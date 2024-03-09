import flet as ft
import flet.canvas as cv
from Tools import LineTool, State
from flet_contrib.color_picker import ColorPicker
class Holst(ft.UserControl):
    def __init__(self, color_picker:ColorPicker,color="#000000",tool=LineTool()):
        super().__init__()
        self.tool = tool
        self.state = State()
        self.color = color
        self.color_picker = color_picker
    def build(self):
        # Главный холст для рисования
        self.holst = cv.Canvas(
            shapes=[
                cv.Fill(
                    ft.Paint(
                        gradient=ft.PaintLinearGradient(
                            (0, 0), (600, 600), colors=[ft.colors.CYAN_50, ft.colors.GREY]
                        )
                    )
                )
            ],
            # обработка событий на холсте
            content=ft.GestureDetector(
                on_pan_start=self.pan_start,
                on_pan_update=self.pan_update,
                drag_interval=10
            ),
            expand=False,
        )
        return self.holst

    def pan_start(self, e: ft.DragStartEvent):
        self.state.x = e.local_x
        self.state.y = e.local_y
        self.color = self.color_picker.color

    def pan_update(self, e: ft.DragUpdateEvent):
        self.tool.draw(
            self.holst,
            start_x=self.state.x,
            start_y=self.state.y,
            end_x=e.local_x,
            end_y=e.local_y,
            color = self.color,
            stroke_width=3
        )
        self.state.x = e.local_x
        self.state.y = e.local_y