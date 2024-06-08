from abc import ABCMeta, abstractmethod
import toga

class IXmlMod(metaclass=ABCMeta):
    """
    Interface for a mod represented as an XML file.
    
    This interface is used to mark a class as a mod that can be converted to an XML file.
    """

    @property
    @abstractmethod
    def get_path(self) -> str:
        """
        Returns the path of the mod including the file name.
        """
        pass

    @property
    @abstractmethod
    def get_xml(self) -> str:
        """
        Returns the XML content of the mod as a string.
        """
        pass

class IXmlBuilder(metaclass=ABCMeta):
    """
    Interface for a mod builder.

    Classes extending this class are used to build a mod object.
    """
    @property
    @abstractmethod
    def build_xml_mod(self) -> IXmlMod:
        """
        Creates the mod as an XmlMod object.
        """
        pass

class IViewComponent(metaclass=ABCMeta):
    """
    Interface for a view component.

    Classes extending this class are used to create a view component.
    """
    @abstractmethod
    def __init__(self, main_window: toga.MainWindow):
        """
        Initializes the view component.
        """
        self.main_window = main_window
    
    @abstractmethod
    def validation_callback(self, callback):
        """
        Sets the validity of the component.
        """
        pass

    @abstractmethod
    def load_data(self, data: dict):
        """
        Loads data into the component.
        """
        pass

    @abstractmethod
    def save_data(self) -> dict:
        """
        Saves data from the component.
        """
        pass

    @property
    @abstractmethod
    def component(self) -> toga.Box:
        """
        Returns the view component.
        """
        pass