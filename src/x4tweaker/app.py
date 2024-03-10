"""
X4 XML Tweaker
"""
from tkinter import HIDDEN
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW

from x4tweaker.lib.bundler import ModBundle
from x4tweaker.lib.constants import Dlc, SWeapons
from x4tweaker.lib.class_xml_mod_metadata import XmlMetadataBuilder

class X4Tweaker(toga.App):
    def startup(self):
        main_box = toga.Box(style=Pack(direction=COLUMN, padding=10))

        self.xml_content_builder = XmlMetadataBuilder()

        option_container_metadata = toga.Box(style=Pack(direction=COLUMN, padding=5)) # mod name, version, etc.
        self.option_container_weapons = toga.Box(style=Pack(direction=COLUMN))
        option_container_turrets = toga.Box(style=Pack(direction=COLUMN))
        option_container_shields = toga.Box(style=Pack(direction=COLUMN))
        option_container_engines = toga.Box(style=Pack(direction=COLUMN))

        container = toga.OptionContainer(
            content=[
                ("Mod Details", option_container_metadata),
                ("Weapons", self.option_container_weapons),
                ("Turrets", option_container_turrets),
                ("Shields", option_container_shields),
                ("Engines", option_container_engines)

            ],
            style=Pack(height=500)
        )

        option_container_metadata_name = toga.Box(style=Pack(direction=ROW, padding=5))
        name_label = toga.Label(
            "Mod name: ",
            style=Pack(padding=(0, 5), width=100)
        )
        self.mod_name_input = toga.TextInput(style=Pack(flex=1))
        option_container_metadata_name.add(name_label)
        option_container_metadata_name.add(self.mod_name_input)

        option_container_metadata_version = toga.Box(style=Pack(direction=ROW, padding=5))
        version_label = toga.Label(
            "Mod version: ",
            style=Pack(padding=(0, 5), width=100)
        )
        self.mod_version_input = toga.TextInput(style=Pack(flex=1))
        option_container_metadata_version.add(version_label)
        option_container_metadata_version.add(self.mod_version_input)

        option_container_metadata_description = toga.Box(style=Pack(direction=ROW, padding=5))
        description_label = toga.Label(
            "Mod description: ",
            style=Pack(padding=(0, 5), width=100)
        )
        self.mod_description_input = toga.MultilineTextInput(style=Pack(flex=1))
        option_container_metadata_description.add(description_label)
        option_container_metadata_description.add(self.mod_description_input)

        option_container_metadata_author = toga.Box(style=Pack(direction=ROW, padding=5))
        author_label = toga.Label(
            "Mod author: ",
            style=Pack(padding=(0, 5), width = 100)
        )
        self.mod_author_input = toga.TextInput(style=Pack(flex=1))
        option_container_metadata_author.add(author_label)
        option_container_metadata_author.add(self.mod_author_input)

        option_container_metadata_date = toga.Box(style=Pack(direction=ROW, padding=5))
        date_label = toga.Label(
            "Date: ",
            style=Pack(padding=(0, 5), width = 100)
        )
        self.mod_date_input = toga.TextInput(style=Pack(flex=1), placeholder="YYYY-MM-DD")
        option_container_metadata_date.add(date_label)
        option_container_metadata_date.add(self.mod_date_input)

        option_container_metadata_save = toga.Box(style=Pack(direction=ROW, padding=5))
        save_label = toga.Label(
            "Save compatible? ",
            style=Pack(padding=(0, 5), width=100)
        )
        self.mod_save_switch = toga.Switch("Yes")
        option_container_metadata_save.add(save_label)
        option_container_metadata_save.add(self.mod_save_switch)

        option_container_metadata.add(option_container_metadata_name)
        option_container_metadata.add(option_container_metadata_description)
        option_container_metadata.add(option_container_metadata_author)
        option_container_metadata.add(option_container_metadata_version)
        option_container_metadata.add(option_container_metadata_date)
        option_container_metadata.add(option_container_metadata_save)

        option_container_metadata.add(toga.Divider(style=Pack(padding=10)))

        option_container_metadata.add(toga.Label("Compatible DLCs:", style=Pack(padding=(4, 5))))

        dlc_options = toga.ScrollContainer(content=toga.Box(children=[
            toga.Switch(id=dlc.value[0], text=dlc.value[1], on_change=self.add_dlc_requirement) for dlc in Dlc
        ], style=Pack(direction=COLUMN, padding=5)))

        option_container_metadata.add(dlc_options)

        option_container_metadata.add(toga.Divider(style=Pack(padding=10)))


        # Weapons Tab Data

        weapon_class_selector = toga.Selection(items=["Chose...", "SMALL", "MEDIUM", "LARGE"], on_change=self.toggle_weapon_class_view)
        self.option_container_weapons.add(weapon_class_selector)

        self.weapons_s_box = toga.Box(style=Pack(direction=COLUMN), id="weapons_s_box")
        self.weapons_m_box = toga.Box(style=Pack(direction=COLUMN), id="weapons_m_box")
        self.weapons_l_box = toga.Box(style=Pack(direction=COLUMN), id="weapons_l_box")

        self.weapons_m_box.add(toga.Label("M BOX", style=Pack(padding=(4, 5))))


        self.weapons_s_box.add(toga.Label("Which weapons do you wish to edit?", style=Pack(padding=(4, 5))))

        weapon_options = toga.ScrollContainer(content=toga.Box(children=[
            toga.Switch(id=weapon_small.value[0], text=weapon_small.value[1]) for weapon_small in SWeapons
        ], style=Pack(direction=COLUMN, padding=5)))
        self.weapons_s_box.add(weapon_options)

        button = toga.Button(
            "Generate",
            on_press=self.generate_mod,
            style=Pack(padding=5)
        )

        main_box.add(container)
        main_box.add(button)

        self.main_window = toga.MainWindow(title=self.formal_name, size=(800, 600), resizable=False)
        self.main_window.content = main_box
        self.main_window.show()
    
    def add_dlc_requirement(self, widget: toga.Switch):
        self.xml_content_builder.add_dlc_requirement(widget.id, widget.value)

    def toggle_weapon_class_view(self, widget: toga.Selection):
        match widget.value:
            case "SMALL":
                self.option_container_weapons.add(self.weapons_s_box)
                self.option_container_weapons.remove(self.weapons_m_box)
                self.option_container_weapons.remove(self.weapons_l_box)
            case "MEDIUM":
                self.option_container_weapons.remove(self.weapons_s_box)
                self.option_container_weapons.add(self.weapons_m_box)
                self.option_container_weapons.remove(self.weapons_l_box)
            case "LARGE":
                self.option_container_weapons.remove(self.weapons_s_box)
                self.option_container_weapons.remove(self.weapons_m_box)
                self.option_container_weapons.add(self.weapons_l_box)
            case _:
                self.option_container_weapons.remove(self.weapons_s_box)
                self.option_container_weapons.remove(self.weapons_m_box)
                self.option_container_weapons.remove(self.weapons_l_box)

    async def generate_mod(self, widget):
        metadata = self.xml_content_builder\
            .add_name(self.mod_name_input.value)\
            .add_version(self.mod_version_input.value)\
            .add_description(self.mod_description_input.value)\
            .add_author(self.mod_author_input.value)\
            .add_date(self.mod_date_input.value)\
            .add_save_compatibility(self.mod_save_switch.value)\
            .build_xml_mod()
        
        try:
            path_name = await self.main_window.save_file_dialog(file_types=["zip"], title="Save mod", suggested_filename=self.mod_name_input.value)
            if path_name is not None:
                ModBundle(bundle_name=self.mod_name_input.value, bundle_output_path=path_name).add_xml(metadata).build()
                await self.main_window.info_dialog("X4 Tweaker", "Mod created successfully!")
        except ValueError:
            await self.main_window.error_dialog("X4 Tweaker", "Could not select folder. Please try again.")

def main():
    return X4Tweaker()

# github actions: https://github.com/beeware/briefcase/issues/945