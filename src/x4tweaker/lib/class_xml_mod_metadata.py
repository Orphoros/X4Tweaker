import xml.dom.minidom
from xml.etree.ElementTree import Element, SubElement, tostring
import os.path

from x4tweaker.lib.constants import Dlc
from x4tweaker.lib.interfaces import IXmlBuilder, IXmlMod

class XmlMetadata(IXmlMod):
    def __init__(self, bundle_name: str, bundle_contents: str, bundle_output_path = "") -> None:
        self.name = bundle_name
        self.output_path = bundle_output_path
        self.xml = bundle_contents

    @property
    def get_path(self) -> str:
        return os.path.join(self.output_path, self.name)

    @property
    def get_xml(self) -> str:
        return self.xml

class XmlMetadataBuilder(IXmlBuilder):
    def __init__(self) -> None:
        self.content = Element('content')
        self.list_dlc_required = []

        for dlc in Dlc:
            id = dlc.value[0]
            name = dlc.value[1]
            element = SubElement(self.content, "dependency")
            element.set("id", id)
            element.set("name", name)
            element.set("optional", "true")

        # TODO: Add ID
        # TODO: Add date

    def add_name(self, name: str):
        self.content.set("name", name)
        return self

    def add_version(self, version: str):
        self.content.set("version", version)
        return self

    def add_description(self, description: str):
        self.content.set("description", description)
        return self
    
    def add_author(self, author: str):
        self.content.set("author", author)
        return self
    
    def add_date(self, date: str):
        self.content.set("date", date)
        return self

    def add_version(self, version: str):
        self.content.set("version", version)
        return self

    def add_save_compatibility(self, save_compatible: bool):
        self.content.set("save", "1" if save_compatible else "0")
        return self

    def add_dlc_requirement(self, dlc: str, required: bool):
        self.content.find(".//dependency[@id='" + dlc + "']").set("optional", "false" if required else "true")
        # add dlc to list of required dlcs if not already in list
        if required and dlc not in self.list_dlc_required:
            self.list_dlc_required.append(dlc)
        return self

    def build_xml_mod(self) -> IXmlMod:
        str = tostring(self.content, encoding='unicode')
        dom = xml.dom.minidom.parseString(str)
        str_formatted = dom.toprettyxml()
        return XmlMetadata(bundle_name="content.xml", bundle_contents=str_formatted)