import flet as ft
from flet import UserControl

class SideBar(UserControl):
    def __init__(self):
        super().__init__()
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
            selected_index=1,
            animation_duration=300,
            tabs=[
                ft.Tab(
                    text="Tab 1",
                    content=ft.Container(
                        content=ft.Text("This is Tab 1"), alignment=ft.alignment.center
                    ),
                ),
                ft.Tab(
                    tab_content=ft.Icon(ft.icons.SEARCH),
                    content=ft.Text("This is Tab 2"),
                ),
                ft.Tab(
                    text="Tab 3",
                    icon=ft.icons.SETTINGS,
                    content=ft.Text("This is Tab 3"),
                ),
            ],
        )