import toga
from toga.style import Pack
from toga.style.pack import COLUMN
from x4tweaker.lib.bundler import ModBundle
from x4tweaker.lib.class_xml_mod_metadata import XmlMetadataBuilder
from x4tweaker.lib.interfaces import IViewComponent
from x4tweaker.views.submenus import MetadataSubView, WeaponsSubView, TurretsSubView, ShieldsSubView, EnginesSubView

class MainView (IViewComponent):
    def __init__(self, main_window: toga.MainWindow):
        super().__init__(main_window)
        self.xml_content_builder = XmlMetadataBuilder()
        self.main_box = toga.Box(style=Pack(direction=COLUMN, padding=10))

        self.metadata_sub_view = MetadataSubView(self.main_window, self.xml_content_builder)
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

        self.generate_btn = toga.Button(
            "Generate",
            on_press=self.generate_mod,
            style=Pack(padding=5)
        )
    
    async def generate_mod(self, widget):
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

    @property
    def component(self):
        self.main_box.add(self.submenus)
        self.main_box.add(self.generate_btn)

        return self.main_box
