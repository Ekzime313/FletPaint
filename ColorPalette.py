import flet as ft
from flet_contrib.color_picker import ColorPicker

class ColorPalette():
    def __init__(self):
        self.color_picker = ColorPicker('#000000')

    def build(self):
        return ft.Column(
            controls=[self.color_picker]
        )

