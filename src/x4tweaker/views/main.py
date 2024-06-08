import os
import toga
import joblib
from toga.style import Pack
from toga.style.pack import COLUMN
from x4tweaker.lib.bundler import ModBundle
from x4tweaker.lib.class_xml_mod_metadata import XmlMetadataBuilder
from x4tweaker.lib.interfaces import IViewComponent
from x4tweaker.views.submenus import MetadataSubView, WeaponsSubView, TurretsSubView, ShieldsSubView, EnginesSubView

class MainView (IViewComponent):
    def __init__(self, main_window: toga.MainWindow):
        super().__init__(main_window)
        self.__define_commands()
        self.xml_content_builder = XmlMetadataBuilder()
        self.main_box = toga.Box(style=Pack(direction=COLUMN, padding=10))

        self.metadata_sub_view = MetadataSubView(self.main_window, self.xml_content_builder)
        self.metadata_sub_view.validation_callback(self.__control_button)
        self.weapons_sub_view = WeaponsSubView(self.main_window)
        self.turrets_sub_view = TurretsSubView(self.main_window)
        self.shields_sub_view = ShieldsSubView(self.main_window)
        self.engines_sub_view = EnginesSubView(self.main_window)

        self.submenus = toga.OptionContainer(
            content=[
                ("Mod Details", self.metadata_sub_view.component),
                ("Weapons", self.weapons_sub_view.component),
                ("Turrets", self.turrets_sub_view.component),
                ("Shields", self.shields_sub_view.component),
                ("Engines", self.engines_sub_view.component)

            ],
            style=Pack(height=500)
        )
    
    def __control_button(self, is_valid: bool):
        self.save_command.enabled = is_valid
    
    def __define_commands(self):
        self.bundle_icon = 'resources/icon_bundle.png'
        self.open_icon = 'resources/icon_open.png'
        self.save_icon = 'resources/icon_save.png'

        self.save_command = toga.Command(
            self.__generate_mod,
            text='Generate',
            tooltip='Generate mod',
            enabled=True,
            shortcut=toga.Key.MOD_1 + 'g',
            icon=self.bundle_icon
        )

        self.generate_command = toga.Command(
            self.__save_project,
            text='Save',
            tooltip='Save project',
            enabled=True,
            shortcut=toga.Key.MOD_1 + 's',
            icon=self.save_icon
        )

        self.open_command = toga.Command(
            self.__open_project,
            text='Open',
            tooltip='Open project',
            enabled=True,
            shortcut=toga.Key.MOD_1 + 'o',
            icon=self.open_icon
        )

        self.main_window.toolbar.add(self.open_command)
        self.main_window.toolbar.add(self.generate_command)
        self.main_window.toolbar.add(self.save_command)
    
    async def __open_project(self, widget):
        try:
            path_name = await self.main_window.open_file_dialog(file_types=["x4t"], title="Open project")
            if path_name is not None:
                data = joblib.load(path_name)
                self.metadata_sub_view.load_data(data["metadata"])
                await self.main_window.info_dialog("X4 Tweaker", "Project loaded successfully!")
        except ValueError:
            await self.main_window.error_dialog("X4 Tweaker", "Could not select folder. Please try again.")
    
    async def __save_project(self, widget):
        dict = {}
        dict["metadata"] = self.metadata_sub_view.save_data()
        
        try:
            path_name = await self.main_window.save_file_dialog(file_types=["x4t"], title="Save project", suggested_filename=dict["metadata"]["name"])
            if path_name is not None:
                path = os.path.splitext(path_name)[0]
                joblib.dump(dict, path + ".x4t")
                await self.main_window.info_dialog("X4 Tweaker", "Project saved successfully!")
        except ValueError:
            await self.main_window.error_dialog("X4 Tweaker", "Could not select folder. Please try again.")
    
    async def __generate_mod(self, widget):
        metadata = self.xml_content_builder\
            .add_name(self.metadata_sub_view.mod_name_input.value)\
            .add_version(self.metadata_sub_view.mod_version_input.value)\
            .add_description(self.metadata_sub_view.mod_description_input.value)\
            .add_author(self.metadata_sub_view.mod_author_input.value)\
            .add_date(self.metadata_sub_view.mod_date_input.value)\
            .add_save_compatibility(self.metadata_sub_view.mod_save_compatible.value)\
            .build_xml_mod()
        
        try:
            path_name = await self.main_window.save_file_dialog(file_types=["zip"], title="Save mod", suggested_filename=self.metadata_sub_view.mod_name_input.value)
            if path_name is not None:
                ModBundle(bundle_name=self.metadata_sub_view.mod_name_input.value, bundle_output_path=path_name).add_xml(metadata).build()
                await self.main_window.info_dialog("X4 Tweaker", "Mod created successfully!")
        except ValueError:
            await self.main_window.error_dialog("X4 Tweaker", "Could not select folder. Please try again.")
    
    def validation_callback(self, callback):
        pass

    def load_data(self, data: dict):
        pass

    def save_data(self) -> dict:
        pass


    @property
    def component(self):
        self.main_box.add(self.submenus)

        return self.main_box
