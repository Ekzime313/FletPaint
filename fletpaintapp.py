from typing import Final
import flet as ft
from flet import Container
from holst import Holst
from menubar import MenuBar
from sidebar import SideBar
from flet_contrib.color_picker import ColorPicker
from switchshape import SwitchShape

TITLE: Final[str] = "Flet Paint"

class PaintApp():
    def __init__(self,page:ft.Page):
        self.page = page
        self.page.title = TITLE

        self.size_list = self.create_size_list()

        self.color_picker = ColorPicker("#000000")
        self.switchshape_bt = SwitchShape()
        self.holst = Holst(color_picker=self.color_picker, size_list=self.size_list)
        self.sidebar = SideBar(color_picker=self.color_picker,
                               size_list=self.size_list,
                               switchshape=self.switchshape_bt)
        self.menubar = MenuBar()

        self.build()

    def build(self):
        holst_view = self.create_holst_view(holst=self.holst)

        self.page.add(self.menubar,
                      self.create_page_content(holst_view, self.sidebar)
                      )
        self.page.update()

    def create_holst_view(self,holst: Holst) -> Container:
        return Container(
            holst,
            border_radius=5,
            width=float("inf"),
            expand=True,
        )

    def create_page_content(self,holst_view: ft.Container, sidebar: SideBar) -> ft.Row:
        return ft.Row(
            controls=[
                Container(
                    holst_view,
                    padding=20,
                    expand=True
                ),
                sidebar
            ],
            expand=True
        )
    def create_size_list(self) -> ft.Dropdown:
        return ft.Dropdown(
            width=108,
            label="size",
            value="3",
            options=[
                ft.dropdown.Option("1"),
                ft.dropdown.Option("3"),
                ft.dropdown.Option("5"),
                ft.dropdown.Option("7"),
                ft.dropdown.Option("9"),
                ft.dropdown.Option("11"),
                ft.dropdown.Option("13"),
                ft.dropdown.Option("15"),
                ft.dropdown.Option("17"),
            ],
        )