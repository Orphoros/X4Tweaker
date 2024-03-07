"""
X4 XML Tweaker
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW

class X4Tweaker(toga.App):
    def startup(self):
        main_box = toga.Box(style=Pack(direction=COLUMN, padding=10))

        option_container_metadata = toga.Box(style=Pack(direction=COLUMN, padding=5)) # mod name, version, etc.
        option_container_weapons = toga.Box(style=Pack(direction=COLUMN))

        container = toga.OptionContainer(
            content=[
                ("Mod Details", option_container_metadata),
                ("Weapons",option_container_weapons)
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

        option_container_metadata_save = toga.Box(style=Pack(direction=ROW, padding=5))
        save_label = toga.Label(
            "Save compatible? ",
            style=Pack(padding=(0, 5), width=100)
        )
        self.mod_save_switch = toga.Switch("No/Yes")
        option_container_metadata_save.add(save_label)
        option_container_metadata_save.add(self.mod_save_switch)

        option_container_metadata.add(option_container_metadata_name)
        option_container_metadata.add(option_container_metadata_description)
        option_container_metadata.add(option_container_metadata_author)
        option_container_metadata.add(option_container_metadata_version)
        option_container_metadata.add(option_container_metadata_save)

        option_container_metadata.add(toga.Divider(style=Pack(padding=10)))

        option_container_metadata.add(toga.Label("Compatible DLCs:", style=Pack(padding=(4, 5))))

        dlc_options = toga.ScrollContainer(content=toga.Box(children=[
            toga.Switch("X4: Split Vendetta"),
            toga.Switch("X4: Cradle of Humanity"),
            toga.Switch("X4: Kingdom End"),
            toga.Switch("X4: Timelines"),
            toga.Switch("X4: Tides of Avarice")
        ], style=Pack(direction=COLUMN, padding=5)))

        option_container_metadata.add(dlc_options)

        option_container_metadata.add(toga.Divider(style=Pack(padding=10)))

        button = toga.Button(
            "Generate",
            on_press=self.say_hello,
            style=Pack(padding=5)
        )

        main_box.add(container)
        # main_box.add(button)

        self.main_window = toga.MainWindow(title=self.formal_name, size=(800, 600), resizable=False)
        self.main_window.content = main_box
        self.main_window.show()

    def say_hello(self, widget):
        print('Generate button clicked')


def main():
    return X4Tweaker()

# github actions: https://github.com/beeware/briefcase/issues/945