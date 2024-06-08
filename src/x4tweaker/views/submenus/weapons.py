import toga
from toga.style import Pack
from toga.style.pack import COLUMN
from x4tweaker.lib.interfaces import IViewComponent

class WeaponsSubView (IViewComponent):
    def __init__(self, main_window: toga.MainWindow):
        super().__init__(main_window)

        self.metadata_box = toga.Box(style=Pack(direction=COLUMN, padding=5))

    def __define_comp_weapon_selector(self) -> toga.Box:
        self.weapon_class_selection = toga.Selection(items=["Chose...", "SMALL", "MEDIUM", "LARGE"], on_change=self.__toggle_weapon_class_view)
        return self.weapon_class_selection
    
    def __define_comp_option_container_weapons(self) -> toga.Box:
        self.option_container_weapons = toga.Box(style=Pack(direction=COLUMN, padding=5))
        self.option_container_weapons.add(self.__define_comp_default_none_selection())
        return self.option_container_weapons
    
    def __define_comp_default_none_selection(self) -> toga.Box:
        self.default_none_selection = toga.Box(style=Pack(direction=COLUMN), id="default_none_selection")
        self.default_none_selection.add(toga.Label("Which weapons do you wish to edit?", style=Pack(padding=(4, 5))))
        return self.default_none_selection
    
    def __define_comp_weapons_s_box(self) -> toga.Box:
        self.weapons_s_box = toga.Box(style=Pack(direction=COLUMN), id="weapons_s_box")
        self.weapons_s_box.add(toga.Label("S BOX", style=Pack(padding=(4, 5))))
        return self.weapons_s_box

    def __define_comp_weapons_m_box(self) -> toga.Box:
        self.weapons_m_box = toga.Box(style=Pack(direction=COLUMN), id="weapons_m_box")
        self.weapons_m_box.add(toga.Label("M BOX", style=Pack(padding=(4, 5))))
        return self.weapons_m_box

    def __define_comp_weapons_l_box(self) -> toga.Box:
        self.weapons_l_box = toga.Box(style=Pack(direction=COLUMN), id="weapons_l_box")
        self.weapons_l_box.add(toga.Label("L BOX", style=Pack(padding=(4, 5))))
        return self.weapons_l_box

    def __toggle_weapon_class_view(self, widget: toga.Selection):
        match widget.value:
            case "SMALL":
                self.option_container_weapons.add(self.weapons_s_box)
                self.option_container_weapons.remove(self.weapons_m_box)
                self.option_container_weapons.remove(self.weapons_l_box)
                self.option_container_weapons.remove(self.default_none_selection)
            case "MEDIUM":
                self.option_container_weapons.remove(self.weapons_s_box)
                self.option_container_weapons.add(self.weapons_m_box)
                self.option_container_weapons.remove(self.weapons_l_box)
                self.option_container_weapons.remove(self.default_none_selection)
            case "LARGE":
                self.option_container_weapons.remove(self.weapons_s_box)
                self.option_container_weapons.remove(self.weapons_m_box)
                self.option_container_weapons.add(self.weapons_l_box)
                self.option_container_weapons.remove(self.default_none_selection)
            case _:
                self.option_container_weapons.remove(self.weapons_s_box)
                self.option_container_weapons.remove(self.weapons_m_box)
                self.option_container_weapons.remove(self.weapons_l_box)
                self.option_container_weapons.add(self.default_none_selection)

    @property
    def component(self):
        self.__define_comp_weapons_l_box()
        self.__define_comp_weapons_m_box()
        self.__define_comp_weapons_s_box()
        self.metadata_box.add(self.__define_comp_weapon_selector())
        self.metadata_box.add(self.__define_comp_option_container_weapons())

        return self.metadata_box

    def validation_callback(self, callback):
        pass

    def load_data(self, data: dict):
        pass

    def save_data(self) -> dict:
        pass
