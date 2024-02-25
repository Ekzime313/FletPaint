from typing import Final
import flet as ft
from flet import Container
from holst import Holst

TITLE: Final[str] = "Flet Paint"

def create_holst_view(holst: Holst) -> Container:
    """
    Функция create_holst_view, которая:

    * Создает контейнер для холста.
    * Устанавливает радиус границы контейнера.
    * Устанавливает ширину контейнера в бесконечность.
    * Растягивает контейнер по горизонтали.

    Args:
        holst: Экземпляр класса Holst, который представляет собой холст для рисования.

    Returns:
        Экземпляр класса Container, который представляет собой контейнер для холста.
    """
    return Container(
        holst,
        border_radius=5,
        width=float("inf"),
        expand=True,
    )

def create_page_content(holst_view: Container) -> Container:
    """
    Функция create_page_content, которая:

    * Создает контейнер для содержимого страницы.
    * Добавляет контейнер с холстом в контейнер для содержимого страницы.
    * Устанавливает отступы контейнера.
    * Растягивает контейнер по горизонтали и вертикали.

    Args:
        holst_view: Экземпляр класса Container, который представляет собой контейнер для холста.

    Returns:
        Экземпляр класса Container, который представляет собой контейнер для содержимого страницы.
    """
    return Container(
            holst_view,
            padding=20,
            expand=True
        )

def main(page:ft.Page):
    page.title =TITLE

    holst = Holst()
    holst_view = create_holst_view(holst)

    page.add(create_page_content(holst_view))

ft.app(target=main)