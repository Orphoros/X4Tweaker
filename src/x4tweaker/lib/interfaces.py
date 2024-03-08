class IXmlMod:
    """
    Interface for a mod represented as an XML file.
    
    This interface is used to mark a class as a mod that can be converted to an XML file.
    """

    @property
    def get_path(self) -> str:
        """
        Returns the path of the mod including the file name.
        """
        pass
    @property
    def get_xml(self) -> str:
        """
        Returns the XML content of the mod as a string.
        """
        pass

class IXmlBuilder:
    """
    Interface for a mod builder.

    Classes extending this class are used to build a mod object.
    """
    @property
    def build_xml_mod(self) -> IXmlMod:
        """
        Creates the mod as an XmlMod object.
        """
        pass
