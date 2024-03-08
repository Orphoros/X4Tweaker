import xml.dom.minidom
from xml.etree.ElementTree import Element, SubElement, tostring
import os.path

from x4tweaker.lib.interfaces import IXmlBuilder, IXmlMod

class XmlMetadata(IXmlMod):
    def __init__(self, bundle_name: str, bundle_contents: str, bundle_output_path = ".") -> None:
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
        self.root = Element('root')
        self.mod = SubElement(self.root, "child")
        self.mods = []

    def add_name(self, name: str):
        SubElement(self.mod, "name").text = name
        return self

    def add_version(self, version: str):
        SubElement(self.mod, "version").text = version
        return self

    def add_description(self, description: str):
        SubElement(self.mod, "description").text = description
        return self
    
    def add_author(self, author: str):
        SubElement(self.mod, "author").text = author
        return self

    def add_version(self, version: str):
        SubElement(self.mod, "version").text = version
        return self

    def add_savable(self, savable: bool):
        SubElement(self.mod, "savable").text = str(savable)
        return self

    def add_mod_compatibility(self, mod: str):
        if mod not in self.mods:
            self.mods.append(mod)
        return self

    def build_xml_mod(self) -> IXmlMod:
        SubElement(self.mod, "mod_compatibility").text = ', '.join(self.mods)
        str = tostring(self.root, encoding='unicode')
        dom = xml.dom.minidom.parseString(str)
        str_formatted = dom.toprettyxml()
        return XmlMetadata(bundle_name="metadata.xml", bundle_contents=str_formatted)