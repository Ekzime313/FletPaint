import flet as ft
from flet import (UserControl)
class MenuBar(UserControl):
    def __init__(self):
        super().__init__()

        self.panel_on = True

        self.menubar = ft.MenuBar(
            style=ft.MenuStyle(
                alignment=ft.alignment.top_left,
                bgcolor=ft.colors.BLUE_GREY_900,
                mouse_cursor={
                    ft.MaterialState.HOVERED: ft.MouseCursor.WAIT,
                    ft.MaterialState.DEFAULT: ft.MouseCursor.ZOOM_OUT,
                },
            ),
        )

    def build(self):
        self.menubar.expand= True
        self.menubar.controls=[
                ft.SubmenuButton(
                    content=ft.Text("File",color=ft.colors.BLUE_GREY_200),
                    controls=[
                        ft.MenuItemButton(
                            content=ft.Text("About",color=ft.colors.BLUE_GREY_200),
                            leading=ft.Icon(ft.icons.INFO),
                            on_click=self.bt_click,
                            style=ft.ButtonStyle(
                                bgcolor={ft.MaterialState.HOVERED: ft.colors.BLUE_GREY}
                            ),
                        ),
                        ft.MenuItemButton(
                            content=ft.Text("Save",color=ft.colors.BLUE_GREY_200),
                            leading=ft.Icon(ft.icons.SAVE),
                            on_click=self.bt_click,
                            style=ft.ButtonStyle(
                                bgcolor={ft.MaterialState.HOVERED: ft.colors.BLUE_GREY}
                            ),
                        )
                    ],
                ),
                ft.SubmenuButton(
                    content=ft.Text("Panel",color=ft.colors.BLUE_GREY_200),
                    controls=[
                        ft.MenuItemButton(
                            content=ft.Text("Turn -> off",color=ft.colors.BLUE_GREY_200),
                            leading=ft.Icon(ft.icons.EDIT_NOTE),
                            on_click=self.bt_panel,
                            style=ft.ButtonStyle(
                                bgcolor={ft.MaterialState.HOVERED: ft.colors.BLUE_GREY}
                            ),
                        )
                    ],
                ),
            ]
        return ft.Row(controls=[self.menubar])

    def bt_click(self,e):
        pass
    def bt_panel(self,e):
        if self.panel_on:
            self.menubar.controls[1].controls[0].content = ft.Text(f"Turn -> on",color=ft.colors.BLUE_GREY_200)
            self.panel_on = False
        else:
            self.menubar.controls[1].controls[0].content = ft.Text("Turn -> off", color=ft.colors.BLUE_GREY_200)
            self.panel_on = True
        self.update()