"""
X4 XML Tweaker
"""
import toga
from x4tweaker.views import MainView

class X4Tweaker(toga.App):
    def startup(self):
        self.main_window = toga.MainWindow(title=self.formal_name, size=(800, 600), resizable=False)

        main_box = MainView(self.main_window).component

        self.main_window.content = main_box
        self.main_window.show()

def main():
    return X4Tweaker()
