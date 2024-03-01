import flet as ft
from flet import (UserControl)

class MenuBar(UserControl):
    def __init__(self):
        super().__init__()
        self.menubar = ft.MenuBar()

    def build(self):
        self.menubar.expand= True
        self.menubar.controls=[
                ft.SubmenuButton(
                    content=ft.Text("File"),
                    controls=[
                        ft.MenuItemButton(
                            content=ft.Text("About"),
                            leading=ft.Icon(ft.icons.INFO),
                            on_click=self.bt_click,
                        ),
                        ft.MenuItemButton(
                            content=ft.Text("Save"),
                            leading=ft.Icon(ft.icons.SAVE),
                            on_click=self.bt_click,
                        )
                    ]
                ),
                ft.SubmenuButton(
                    content=ft.Text("Panel"),
                    controls=[
                        ft.MenuItemButton(
                            content=ft.Text("Turn -> off"),
                            leading=ft.Icon(ft.icons.EDIT_NOTE),
                            on_click=self.bt_click,
                        )
                    ]
                )
            ]
        return ft.Row(controls=[self.menubar])

    def bt_click(self,e):
        pass