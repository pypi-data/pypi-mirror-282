"""Output rendering logic.

Note that the Django format_html() / mark_safe() logic is not used here,
as it's quite a performance improvement to just use html.escape().
"""

from __future__ import annotations

import re
from datetime import date, datetime, time, timezone
from io import BytesIO
from typing import cast

from django.contrib.gis import geos
from django.db import models
from django.http import HttpResponse, StreamingHttpResponse
from lxml import etree

from gisserver.db import (
    AsGML,
    build_db_annotations,
    conditional_transform,
    get_db_annotation,
    get_db_geometry_selects,
    get_db_geometry_target,
    get_geometries_union,
)
from gisserver.exceptions import NotFound
from gisserver.features import FeatureRelation, FeatureType
from gisserver.geometries import CRS
from gisserver.parsers.fes20 import ValueReference
from gisserver.types import XsdComplexType, XsdElement

from .base import OutputRenderer
from .results import SimpleFeatureCollection

GML_RENDER_FUNCTIONS = {}
RE_GML_ID = re.compile(r'gml:id="[^"]+"')

WFS_NS = "http://www.opengis.net/wfs/2.0"
GML32_NS = "http://www.opengis.net/gml/3.2"
XSI_NS = "http://www.w3.org/2001/XMLSchema-instance"

FIX_GML_NS = f' xmlns:gml="{GML32_NS}">'

# Avoid string concatenations in code:
XSI_NIL_ATTRIB = {f"{{{XSI_NS}}}nil": "true"}
GML_ID_ATTR = f"{{{GML32_NS}}}id"  # gml:id="..."
WFS_MEMBER = f"{{{WFS_NS}}}member"  # <wfs:member>
GML_BOUNDED_BY = f"{{{GML32_NS}}}boundedBy"  # <gml:boundedBy>
GML_ENVELOPE = f"{{{GML32_NS}}}Envelope"  # <gml:Envelope>
GML_LOWER_CORNER = f"{{{GML32_NS}}}lowerCorner"  # <gml:lowerCorner>
GML_UPPER_CORNER = f"{{{GML32_NS}}}upperCorner"  # <gml:upperCorner>

# register common namespaces globally, that's fine here I guess... *fingers crossed*
# etree.register_namespace("wfs", WFS_NS)
# etree.register_namespace("gml", GML32_NS)
NS_MAP = {
    "wfs": WFS_NS,
    "gml": GML32_NS,
}


def default_if_none(value, default):
    if value is None:
        return default
    else:
        return value


def register_geos_type(geos_type):
    def _inc(func):
        GML_RENDER_FUNCTIONS[geos_type] = func
        return func

    return _inc


class GML32Renderer(OutputRenderer):
    """Render the GetFeature XML output in GML 3.2 format"""

    content_type = "text/xml; charset=utf-8"
    xml_collection_tag = "FeatureCollection"
    chunk_size = 40_000

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.nsmap = {**NS_MAP, "app": self.app_xml_namespace}

    def _make_element(self, node: XsdElement, attrib=None) -> etree.Element:
        tag = f"{{{self.nsmap[node.prefix]}}}{node.name}"  # node.xml_name is prefix:name format.
        return etree.Element(tag, attrib=attrib, nsmap=self.nsmap)

    def _make_feature_element(self, feature_type: FeatureType, attrib=None) -> etree.Element:
        tag = f"{{{self.nsmap[feature_type.xml_prefix]}}}{feature_type.name}"  # node.xml_name is prefix:name format.
        return etree.Element(tag, attrib=attrib, nsmap=self.nsmap)

    def get_response(self):
        """Render the output as streaming response."""
        from gisserver.queries import GetFeatureById

        if isinstance(self.source_query, GetFeatureById):
            # WFS spec requires that GetFeatureById output only returns the contents.
            # The streaming response is avoided here, to allow returning a 404.
            return self.get_standalone_response()
        else:
            # Use default streaming response, with render_stream()
            response = super().get_response()
            if isinstance(response, StreamingHttpResponse):
                response["Content-Encoding"] = "gzip"  # lxml.xmlfile compression
            return response

    def get_standalone_response(self):
        """Render a standalone item, for GetFeatureById"""
        sub_collection = self.collection.results[0]
        self.start_collection(sub_collection)
        instance = sub_collection.first()
        if instance is None:
            raise NotFound("Feature not found.")

        body = self.render_feature(
            feature_type=sub_collection.feature_type,
            instance=instance,
        )

        if isinstance(body, str):
            # Best guess for GetFeatureById combined with
            # GetPropertyValue&VALUEREFERENCE=@gml:id
            return HttpResponse(body, content_type="text/plain")
        else:
            return HttpResponse(
                etree.tostring(body, xml_declaration=True),
                content_type=self.content_type,
            )

    def get_xsi_schema_location(self):
        xsd_typenames = ",".join(
            sub_collection.feature_type.name for sub_collection in self.collection.results
        )

        # These are pairs of "namespace location"
        return (
            f"{self.app_xml_namespace}"
            f" {self.server_url}?SERVICE=WFS&VERSION=2.0.0&REQUEST=DescribeFeatureType&TYPENAMES={xsd_typenames}"
            " http://www.opengis.net/wfs/2.0 http://schemas.opengis.net/wfs/2.0/wfs.xsd"
            " http://www.opengis.net/gml/3.2 http://schemas.opengis.net/gml/3.2.1/gml.xsd"
        )

    def render_stream(self):
        """Render the XML as streaming content.
        This renders the standard <wfs:FeatureCollection> / <wfs:ValueCollection>
        """
        collection = self.collection
        output = BytesIO()
        number_matched = collection.number_matched
        number_returned = collection.number_returned

        root_attrib = {
            f"{{{XSI_NS}}}schemaLocation": self.get_xsi_schema_location(),
            "timestamp": collection.timestamp,
            "numberMatched": (
                str(int(number_matched)) if number_matched is not None else "unknown"
            ),
            "numberReturned": str(number_returned),
        }
        if collection.next:
            root_attrib["next"] = collection.next
        if collection.previous:
            root_attrib["previous"] = collection.previous

        with etree.xmlfile(output) as xml_file:
            xml_file.write_declaration()

            # Either FeatureCollection / ValueCollection
            with xml_file.element(
                f"{{{WFS_NS}}}{self.xml_collection_tag}",
                attrib=root_attrib,
                nsmap=self.nsmap,
            ):
                # no results in all sub collections, means not writing any <wfs:member> tags at all.
                if number_returned:
                    has_multiple_collections = len(collection.results) > 1

                    for sub_collection in collection.results:
                        self.start_collection(sub_collection)  # hook for subclasses

                        if has_multiple_collections:
                            xml_file.write(
                                (
                                    f"<wfs:member>\n"
                                    f"<wfs:{self.xml_collection_tag}"
                                    f' timeStamp="{collection.timestamp}"'
                                    f' numberMatched="{int(sub_collection.number_matched)}"'
                                    f' numberReturned="{int(sub_collection.number_returned)}">\n'
                                ).encode()
                            )

                        for i, instance in enumerate(sub_collection):
                            xml_file.write(
                                self.render_wfs_member(sub_collection.feature_type, instance)
                            )

                            # Only perform a 'yield' every once in a while,
                            # as it goes back-and-forth for writing it to the client.
                            if output.tell() > self.chunk_size:
                                xml_file.flush()
                                xml_chunk = output.getvalue()
                                output.seek(0)
                                output.truncate(0)
                                yield xml_chunk

                        if has_multiple_collections:
                            xml_file.write(
                                f"</wfs:{self.xml_collection_tag}>\n</wfs:member>\n".encode()
                            )

        # xml_file.flush()
        yield output.getvalue()

    def start_collection(self, sub_collection: SimpleFeatureCollection):
        """Hook to allow initialization per feature type"""
        pass

    def render_wfs_member(
        self, feature_type: FeatureType, instance: models.Model
    ) -> etree.Element:
        """Write the full <wfs:member> block."""
        wfs_member_tag = etree.Element(WFS_MEMBER, nsmap=self.nsmap)
        wfs_member_tag.append(self.render_feature(feature_type, instance))
        return wfs_member_tag

    def render_feature(
        self, feature_type: FeatureType, instance: models.Model, nsmap=None
    ) -> etree.Element:
        """Write the contents of the object value.

        This output is typically wrapped in <wfs:member> tags
        unless it's used for a GetPropertyById response.
        """
        self.gml_seq = 0  # need to increment this between write_xml_field calls

        # Write <app:FeatureTypeName> start node
        feature_tag = self._make_feature_element(
            feature_type.xml_name,
            attrib={GML_ID_ATTR: f"{feature_type.name}.{instance.pk}"},
        )

        # Add all base class members, in their correct ordering
        # By having these as XsdElement objects instead of hard-coded writes,
        # the query/filter logic also works for these elements.
        if feature_type.xsd_type.base.is_complex_type:
            for xsd_element in feature_type.xsd_type.base.elements:
                if xsd_element.xml_name == "gml:boundedBy":
                    # Special case for <gml:boundedBy>, so it will render with
                    # the output CRS and can be overwritten with DB-rendered GML.
                    gml = self.render_bounds(feature_type, instance)
                    if gml is not None:
                        feature_tag.append(gml)
                elif xsd_element.is_many:
                    # some <app:...> node that has multiple values
                    feature_tag.extend(self.render_many(feature_type, xsd_element, instance))
                else:
                    # e.g. <gml:name>, or all other <app:...> nodes.
                    feature_tag.append(self.render_xml_field(feature_type, xsd_element, instance))

        # Add all members
        for xsd_element in feature_type.xsd_type.elements:
            if xsd_element.is_many:
                # some <app:...> node that has multiple values
                feature_tag.extend(self.render_many(feature_type, xsd_element, instance))
            else:
                # e.g. <gml:name>, or all other <app:...> nodes.
                feature_tag.append(self.render_xml_field(feature_type, xsd_element, instance))

        return feature_tag

    def render_bounds(self, feature_type, instance) -> etree.Element | None:
        """Render the GML bounds for the complete instance"""
        envelope = feature_type.get_envelope(instance, self.output_crs)
        if envelope is None:
            return None

        bounded_by = etree.Element(GML_BOUNDED_BY, nsmap=self.nsmap)
        envelope = etree.SubElement(
            bounded_by,
            GML_ENVELOPE,
            attrib={"srsDimension": "2", "srsName": self.xml_srs_name},
            nsmap=self.nsmap,
        )
        lower = " ".join(map(str, envelope.lower_corner))
        upper = " ".join(map(str, envelope.upper_corner))
        etree.SubElement(envelope, GML_LOWER_CORNER, nsmap=self.nsmap).text = lower
        etree.SubElement(envelope, GML_UPPER_CORNER, nsmap=self.nsmap).text = upper
        return bounded_by

    def render_many(
        self, feature_type, xsd_element: XsdElement, instance: models.Model
    ) -> list[etree.Element]:
        """Render a single field, multiple times."""
        value = xsd_element.get_value(instance)
        if value is None:
            # No tag for optional element (see PropertyIsNull), otherwise xsi:nil node.
            if xsd_element.min_occurs == 0:
                return []
            else:
                # <app:field xsi:nil="true"/>
                return [self._make_element(xsd_element, attrib=XSI_NIL_ATTRIB)]
        else:
            # Render the tag multiple times
            if xsd_element.type.is_complex_type:
                # If the retrieved QuerySet was not filtered yet, do so now. This can't
                # be done in get_value() because the FeatureType is not known there.
                value = feature_type.filter_related_queryset(value)

            return [
                self.render_xml_field(feature_type, xsd_element, instance=item) for item in value
            ]

    def render_xml_field(
        self, feature_type: FeatureType, xsd_element: XsdElement, instance: models.Model
    ) -> etree.Element:
        """Write the value of a single field."""
        if xsd_element.is_geometry:
            # Short-cirquit, allow overriding:
            return self.render_gml_field(feature_type, xsd_element, instance)

        value = xsd_element.get_value(instance)
        if value is None:
            return self._make_element(xsd_element, attrib=XSI_NIL_ATTRIB)
        elif xsd_element.type.is_complex_type:
            # Expanded foreign relation / dictionary
            return self.render_xml_complex_type(feature_type, xsd_element, value)
        else:
            xml_field = self._make_element(xsd_element)
            xml_field.text = self._value_to_string(value)
            return xml_field  # <app:field>{value}</app:field>

    def _value_to_string(self, value):
        # TODO: can this be a lookup on the XsdElement?
        if isinstance(value, str):
            return value
        elif isinstance(value, datetime):
            return value.astimezone(timezone.utc).isoformat()
        elif isinstance(value, (date, time)):
            return value.isoformat()
        elif isinstance(value, bool):
            return "true" if value else "false"
        else:
            return str(value)

    def render_xml_complex_type(self, feature_type, xsd_element, value) -> etree.Element:
        """Write a single field, that consists of sub elements"""
        xsd_type = cast(XsdComplexType, xsd_element.type)
        field = self._make_element(xsd_element)
        for sub_element in xsd_type.elements:
            if sub_element.is_many:
                field.extend(self.render_many(feature_type, sub_element, instance=value))
            else:
                field.append(self.render_xml_field(feature_type, sub_element, instance=value))

        return field

    def render_gml_field(
        self,
        feature_type: FeatureType,
        xsd_element: XsdElement,
        instance,
    ) -> str:
        """Write the field that holds an GML tag.
        This is a separate function on purpose, so it can be optimized for database-rendering.
        """
        value: geos.GEOSGeometry = xsd_element.get_value(instance)  # take from DB field
        if value is None:
            return self._make_element(xsd_element.xml_name, attrib=XSI_NIL_ATTRIB)

        self.gml_seq += 1
        gml_id = self.get_gml_id(feature_type, instance.pk, seq=self.gml_seq)

        # Reparsing XML is faster than rendering it ourselves,
        # because it avoids a C-API call for every coordinate
        self.output_crs.apply_to(value)
        gml_parsed = etree.XML(value.ogr.gml)
        gml_parsed.attrib[GML_ID_ATTR] = gml_id
        gml_parsed.attrib["srsName"] = self.xml_srs_name  # TODO: needed?

        node = self._make_element(xsd_element)
        node.append(gml_parsed)
        return node

    def get_gml_id(self, feature_type: FeatureType, object_id, seq) -> str:
        """Generate the gml:id value, which is required for GML 3.2 objects."""
        return f"{feature_type.name}.{object_id}.{seq}"


class DBGML32Renderer(GML32Renderer):
    """Faster GetFeature renderer that uses the database to render GML 3.2"""

    @classmethod
    def decorate_queryset(
        cls,
        feature_type: FeatureType,
        queryset: models.QuerySet,
        output_crs: CRS,
        **params,
    ):
        """Update the queryset to let the database render the GML output.
        This is far more efficient then GeoDjango's logic, which performs a
        C-API call for every single coordinate of a geometry.
        """
        queryset = super().decorate_queryset(feature_type, queryset, output_crs, **params)

        # Retrieve geometries as pre-rendered instead.
        gml_elements = feature_type.xsd_type.geometry_elements
        geo_selects = get_db_geometry_selects(gml_elements, output_crs)
        if geo_selects:
            queryset = queryset.defer(*geo_selects.keys()).annotate(
                _as_envelope_gml=cls.get_db_envelope_as_gml(feature_type, queryset, output_crs),
                **build_db_annotations(geo_selects, "_as_gml_{name}", AsGML),
            )

        return queryset

    @classmethod
    def get_prefetch_queryset(
        cls,
        feature_type: FeatureType,
        feature_relation: FeatureRelation,
        output_crs: CRS,
    ) -> models.QuerySet | None:
        """Perform DB annotations for prefetched relations too."""
        base = super().get_prefetch_queryset(feature_type, feature_relation, output_crs)
        if base is None:
            return None

        # Find which fields are GML elements
        gml_elements = []
        for e in feature_relation.xsd_elements:
            if e.is_geometry:
                # Prefetching a flattened relation
                gml_elements.append(e)
            elif e.type.is_complex_type:
                # Prefetching a complex type
                xsd_type: XsdComplexType = cast(XsdComplexType, e.type)
                gml_elements.extend(xsd_type.geometry_elements)

        geometries = get_db_geometry_selects(gml_elements, output_crs)
        if geometries:
            # Exclude geometries from the fields, fetch them as pre-rendered annotations instead.
            return base.defer(geometries.keys()).annotate(
                **build_db_annotations(geometries, "_as_gml_{name}", AsGML),
            )
        else:
            return base

    @classmethod
    def get_db_envelope_as_gml(cls, feature_type, queryset, output_crs) -> AsGML:
        """Offload the GML rendering of the envelope to the database.

        This also avoids offloads the geometry union calculation to the DB.
        """
        geo_fields_union = cls._get_geometries_union(feature_type, queryset, output_crs)
        return AsGML(geo_fields_union, envelope=True)

    @classmethod
    def _get_geometries_union(cls, feature_type: FeatureType, queryset, output_crs):
        """Combine all geometries of the model in a single SQL function."""
        # Apply transforms where needed, in case some geometries use a different SRID.
        return get_geometries_union(
            [
                conditional_transform(
                    model_field.name,
                    model_field.srid,
                    output_srid=output_crs.srid,
                )
                for model_field in feature_type.geometry_fields
            ],
            using=queryset.db,
        )

    def render_gml_field(
        self,
        feature_type: FeatureType,
        xsd_element: XsdElement,
        instance,
        gml_id,
    ) -> str:
        # Optimized path, pre-rendered GML
        # Take from DB annotation instead of DB field.
        gml_text = get_db_annotation(instance, xsd_element.name, "_as_gml_{name}")
        if gml_text is None:
            return self._make_element(xsd_element, attrib=XSI_NIL_ATTRIB)
        else:
            # Extract DB annotation, it needs an gml:id, and have namespaces following ours.
            gml_text = gml_text.replace(">", FIX_GML_NS, 1)  # fix parsing issues
            self.gml_seq += 1
            gml_id = self.get_gml_id(feature_type, instance.pk, seq=self.gml_seq)
            gml_parsed = etree.XML(gml_text)  # TODO: this means re-parsing the string..
            gml_parsed.attrib[GML_ID_ATTR] = gml_id

            node = self._make_element(xsd_element)
            node.append(gml_parsed)
            return node

    def render_bounds(self, feature_type, instance):
        """Generate the <gml:boundedBy> from DB prerendering."""
        gml_text = instance._as_envelope_gml
        if gml_text is not None:
            # TODO: need to reparse here, but can that be avoided??
            gml_text = gml_text.replace(">", FIX_GML_NS, 1)  # fix parsing issues
            bounded_by = etree.Element(GML_BOUNDED_BY, nsmap=self.nsmap)
            bounded_by.append(etree.XML(gml_text))
            return bounded_by
            # return f"<gml:boundedBy>{gml}</gml:boundedBy>\n"


class GML32ValueRenderer(GML32Renderer):
    """Render the GetPropertyValue XML output in GML 3.2 format"""

    content_type = "text/xml; charset=utf-8"
    xml_collection_tag = "ValueCollection"

    def __init__(self, *args, value_reference: ValueReference, **kwargs):
        self.value_reference = value_reference
        super().__init__(*args, **kwargs)
        self.xsd_node = None

    @classmethod
    def decorate_queryset(
        cls,
        feature_type: FeatureType,
        queryset: models.QuerySet,
        output_crs: CRS,
        **params,
    ):
        # Don't optimize queryset, it only retrieves one value
        return queryset

    def start_collection(self, sub_collection: SimpleFeatureCollection):
        # Resolve which XsdNode is being rendered
        match = sub_collection.feature_type.resolve_element(self.value_reference.xpath)
        self.xsd_node = match.child

    def render_wfs_member(
        self, feature_type: FeatureType, instance: dict, extra_xmlns=""
    ) -> etree.Element:
        """Overwritten to handle attribute support."""
        wsf_member = etree.Element(WFS_MEMBER, nsmap=self.nsmap)
        if self.xsd_node.is_attribute:
            # <wfs:member>{value}</wfs:member}
            # When GetPropertyValue selects an attribute, it's value is rendered
            # as plain-text (without spaces!) inside a <wfs:member> element.
            # The format_value() is needed for @gml:id
            body = self.xsd_node.format_raw_value(instance["member"])
            wsf_member.text = body
        else:
            # <wfs:member><app:field>...</app:field></wfs:member>
            # The call to GetPropertyValue selected an element.
            # Render this single element tag inside the <wfs:member> parent.
            wsf_member.append(self.render_feature(feature_type, instance))
        return wsf_member

    def render_feature(
        self, feature_type: FeatureType, instance: dict, extra_xmlns=""
    ) -> etree.ElementTree | str:
        """Write the XML for a single object.
        In this case, it's only a single XML tag.
        """
        value = instance["member"]
        if self.xsd_node.is_geometry:
            gml_id = self.get_gml_id(feature_type, instance["pk"], seq=1)
            return self.render_gml_field(
                feature_type, self.xsd_node, instance=instance, gml_id=gml_id
            )
        else:
            # The xsd_element is needed so write_xml_field() can render complex types.
            if self.xsd_node.is_attribute:
                # For GetFeatureById, allow returning raw values
                value = self.xsd_node.format_raw_value(value)  # needed for @gml:id
                return str(value)
            else:
                return self.render_xml_field(feature_type, cast(XsdElement, self.xsd_node), value)


class DBGML32ValueRenderer(DBGML32Renderer, GML32ValueRenderer):
    """Faster GetPropertyValue renderer that uses the database to render GML 3.2"""

    @classmethod
    def decorate_queryset(cls, feature_type: FeatureType, queryset, output_crs, **params):
        """Update the queryset to let the database render the GML output."""
        value_reference = params["valueReference"]
        match = feature_type.resolve_element(value_reference.xpath)
        if match.child.is_geometry:
            # Add 'gml_member' to point to the pre-rendered GML version.
            return queryset.values(
                "pk", gml_member=AsGML(get_db_geometry_target(match, output_crs))
            )
        else:
            return queryset

    def render_wfs_member(self, feature_type: FeatureType, instance: dict, extra_xmlns="") -> str:
        """Write the XML for a single object."""
        if "gml_member" in instance:
            gml_id = self.get_gml_id(feature_type, instance["pk"], seq=1)
            body = self.render_db_gml_field(
                feature_type,
                self.xsd_node,
                instance["gml_member"],
                gml_id=gml_id,
            )
            return f"<wfs:member>\n{body}</wfs:member>\n"
        else:
            return super().render_wfs_member(feature_type, instance, extra_xmlns=extra_xmlns)
