import toga
from toga.style import Pack
from toga.style.pack import COLUMN
from x4tweaker.lib.interfaces import IViewComponent

class EnginesSubView (IViewComponent):
    def __init__(self, main_window: toga.MainWindow):
        super().__init__(main_window)

        self.engines_box = toga.Box(style=Pack(direction=COLUMN, padding=5))

    def validation_callback(self, callback):
        pass

    def load_data(self, data: dict):
        pass

    def save_data(self) -> dict:
        pass

    @property
    def component(self):
        return self.engines_box
