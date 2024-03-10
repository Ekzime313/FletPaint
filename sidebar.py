import flet as ft
from flet import UserControl
from flet_contrib.color_picker import ColorPicker
from switchshape import SwitchShape

class SideBar(UserControl):
    def __init__(self,color_picker:ColorPicker,
                 size_list:ft.Dropdown,
                 switchshape:SwitchShape):
        super().__init__()

        self.switchshape_bt = switchshape

        self.color_picker = color_picker
        self.size_list = ft.Container(
            size_list,
            padding=10,
        )

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
                        ft.Column(
                            controls=[
                                self.color_picker,
                                self.size_list
                            ]
                        )
                    ),
                ),
                ft.Tab(
                    tab_content=ft.Icon(ft.icons.SHARE),
                    content=ft.Container(
                        self.switchshape_bt,
                        padding=10
                    )
                ),
                ft.Tab(
                    tab_content=ft.Icon(ft.icons.MOVIE),
                    content=ft.Text("This is Tab 3"),
                ),
            ],
        )

