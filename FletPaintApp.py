from typing import Final
import flet as ft
from flet import Container
from holst import Holst
from menubar import MenuBar
from sidebar import SideBar

TITLE: Final[str] = "Flet Paint"

class PaintApp():
    def __init__(self,page:ft.Page):
        self.page = page
        self.page.title = TITLE

        self.holst = Holst()
        self.menubar = MenuBar()
        self.sidebar = SideBar()

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