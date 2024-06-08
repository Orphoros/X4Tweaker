import toga
from toga.style import Pack
from toga.style.pack import COLUMN
from x4tweaker.lib.interfaces import IViewComponent

class TurretsSubView (IViewComponent):
    def __init__(self, main_window: toga.MainWindow):
        super().__init__(main_window)

        self.turrets_box = toga.Box(style=Pack(direction=COLUMN, padding=5))

    @property
    def component(self):
        return self.turrets_box
