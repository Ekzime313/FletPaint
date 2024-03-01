from typing import Final
import flet as ft
from flet import Container
from holst import Holst
from menubar import MenuBar

TITLE: Final[str] = "Flet Paint"

def create_holst_view(holst: Holst) -> Container:
    return Container(
        holst,
        border_radius=5,
        width=float("inf"),
        expand=True,
    )

def create_page_content(holst_view: Container) -> Container:
    return Container(
            holst_view,
            padding=20,
            expand=True
        )

def main(page:ft.Page):
    page.title =TITLE

    holst = Holst()
    menubar = MenuBar()

    holst_view = create_holst_view(holst)

    page.add(menubar,
             create_page_content(holst_view)
             )

ft.app(target=main)