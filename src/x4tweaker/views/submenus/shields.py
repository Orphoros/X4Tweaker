import toga
from toga.style import Pack
from toga.style.pack import COLUMN
from x4tweaker.lib.interfaces import IViewComponent

class ShieldsSubView (IViewComponent):
    def __init__(self, main_window: toga.MainWindow):
        super().__init__(main_window)

        self.shields_box = toga.Box(style=Pack(direction=COLUMN, padding=5))

    def validation_callback(self, callback):
        pass

    @property
    def component(self):
        return self.shields_box
