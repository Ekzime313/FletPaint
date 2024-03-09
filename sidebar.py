import flet as ft
from flet import UserControl
from flet_contrib.color_picker import ColorPicker

class SideBar(UserControl):
    def __init__(self,color_picker:ColorPicker):
        super().__init__()

        self.color_picker = color_picker

        self.sidebar = ft.Container(  # Sidebar container
            self.tabs(),
            bgcolor=ft.colors.BLUE_GREY_700,  # Set background color
            expand=True,
            width=350,
            border_radius=5,
        )
    def build(self):
        return self.sidebar

    def tabs(self):
        return ft.Tabs(
            selected_index=0,
            animation_duration=300,
            tabs=[
                ft.Tab(
                    tab_content=ft.Icon(ft.icons.COLORIZE),
                    content=ft.Container(
                        content=self.color_picker
                    ),
                ),
                ft.Tab(
                    tab_content=ft.Icon(ft.icons.SHARE),
                    content=ft.Text("This is Tab 2"),
                ),
                ft.Tab(
                    tab_content=ft.Icon(ft.icons.MOVIE),
                    icon=ft.icons.SETTINGS,
                    content=ft.Text("This is Tab 3"),
                ),
            ],
        )
