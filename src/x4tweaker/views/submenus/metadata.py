import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from x4tweaker.lib.class_xml_mod_metadata import XmlMetadataBuilder
from x4tweaker.lib.constants import Dlc
from x4tweaker.lib.input_validators import not_empty
from x4tweaker.lib.interfaces import IViewComponent

class MetadataSubView (IViewComponent):
    def __init__(self, main_window: toga.MainWindow, xml_content_builder: XmlMetadataBuilder):
        super().__init__(main_window)
        self.xml_content_builder = xml_content_builder

        self.metadata_box = toga.Box(style=Pack(direction=COLUMN, padding=5))

    def __define_comp_name(self) -> toga.Box:
        option_container_metadata_name = toga.Box(style=Pack(direction=ROW, padding=5))
        name_label = toga.Label(
            "Mod name: ",
            style=Pack(padding=(0, 5), width=100)
        )
        self.mod_name_input = toga.TextInput(style=Pack(flex=1), validators=[not_empty])
        option_container_metadata_name.add(name_label)
        option_container_metadata_name.add(self.mod_name_input)

        return option_container_metadata_name
    
    def __define_comp_version(self) -> toga.Box:
        option_container_metadata_version = toga.Box(style=Pack(direction=ROW, padding=5))
        version_label = toga.Label(
            "Mod version: ",
            style=Pack(padding=(0, 5), width=100)
        )
        self.mod_version_input = toga.TextInput(style=Pack(flex=1), validators=[not_empty])
        option_container_metadata_version.add(version_label)
        option_container_metadata_version.add(self.mod_version_input)

        return option_container_metadata_version

    def __define_comp_description(self) -> toga.Box:
        option_container_metadata_description = toga.Box(style=Pack(direction=ROW, padding=5))
        description_label = toga.Label(
            "Description:",
            style=Pack(padding=(0, 5), width=100)
        )
        self.mod_description_input = toga.MultilineTextInput(style=Pack(flex=1))
        option_container_metadata_description.add(description_label)
        option_container_metadata_description.add(self.mod_description_input)

        return option_container_metadata_description
    
    def __define_comp_author(self) -> toga.Box:
        option_container_metadata_author = toga.Box(style=Pack(direction=ROW, padding=5))
        author_label = toga.Label(
            "Mod author: ",
            style=Pack(padding=(0, 5), width = 100)
        )
        self.mod_author_input = toga.TextInput(style=Pack(flex=1), validators=[not_empty])
        option_container_metadata_author.add(author_label)
        option_container_metadata_author.add(self.mod_author_input)

        return option_container_metadata_author
    
    def __define_comp_date(self) -> toga.Box:
        option_container_metadata_date = toga.Box(style=Pack(direction=ROW, padding=5))
        date_label = toga.Label(
            "Date: ",
            style=Pack(padding=(0, 5), width = 100)
        )
        self.mod_date_input = toga.TextInput(style=Pack(flex=1), placeholder="YYYY-MM-DD", validators=[not_empty])
        option_container_metadata_date.add(date_label)
        option_container_metadata_date.add(self.mod_date_input)

        return option_container_metadata_date
    
    def __define_comp_save_comp(self) -> toga.Box:
        option_container_metadata_save = toga.Box(style=Pack(direction=ROW, padding=5))
        save_label = toga.Label(
            "Save compatible? ",
            style=Pack(padding=(0, 5), width=100)
        )
        self.mod_save_compatible = toga.Switch("Yes")
        option_container_metadata_save.add(save_label)
        option_container_metadata_save.add(self.mod_save_compatible)

        return option_container_metadata_save
    
    def __define_comp_dlc(self) -> toga.Box:
        option_container_metadata_dlc = toga.Box(style=Pack(direction=COLUMN, padding=5))
        option_container_metadata_dlc.add(toga.Label("Compatible DLCs:", style=Pack(padding=(4, 5))))
        self.dlc_options = toga.ScrollContainer(content=toga.Box(children=[
            toga.Switch(id=dlc.value[0], text=dlc.value[1], on_change=self.__add_dlc_requirement) for dlc in Dlc
        ], style=Pack(direction=COLUMN, padding=5)))
        option_container_metadata_dlc.add(self.dlc_options)

        return option_container_metadata_dlc
    
    def __add_dlc_requirement(self, widget: toga.Switch):
        self.xml_content_builder.add_dlc_requirement(widget.id, widget.value)

    def validation_callback(self, callback):
        self.validation_callback = callback
    
    def load_data(self, data: dict):
        self.mod_name_input.value = data.get("name")
        self.mod_description_input.value = data.get("description")
        self.mod_author_input.value = data.get("author")
        self.mod_version_input.value = data.get("version")
        self.mod_date_input.value = data.get("date")
        self.mod_save_compatible.value = data.get("save_compatible", False)
        compatible_dlcs = data.get("compatible_dlcs", [])
        for comp_dlc in self.dlc_options.content.children:
            if comp_dlc.id in compatible_dlcs:
                comp_dlc.value = True
                self.xml_content_builder.add_dlc_requirement(comp_dlc.id, True)
            else:
                comp_dlc.value = False

    def save_data(self) -> dict:
        return {
            "name": self.mod_name_input.value,
            "version": self.mod_version_input.value,
            "description": self.mod_description_input.value,
            "author": self.mod_author_input.value,
            "date": self.mod_date_input.value,
            "save_compatible": self.mod_save_compatible.value,
            "compatible_dlcs": self.xml_content_builder.list_dlc_required,
        }

    @property
    def component(self):
        self.metadata_box.add(self.__define_comp_name())
        self.metadata_box.add(self.__define_comp_description())
        self.metadata_box.add(self.__define_comp_author())
        self.metadata_box.add(self.__define_comp_version())
        self.metadata_box.add(self.__define_comp_date())
        self.metadata_box.add(self.__define_comp_save_comp())
        self.metadata_box.add(toga.Divider(style=Pack(padding=10)))
        self.metadata_box.add(self.__define_comp_dlc())
        self.metadata_box.add(toga.Divider(style=Pack(padding=10)))

        return self.metadata_box
