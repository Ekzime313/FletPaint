from FletPaintApp import PaintApp
import flet as ft

def main(page:ft.Page):
    paint = PaintApp(page=page)

ft.app(target=main)