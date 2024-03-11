import flet as ft
import flet.canvas as cv
from Tools import DrawingTool
from flet_contrib.color_picker import ColorPicker
from current_draw_tool import StateDraw,StateFlag
class Holst(ft.UserControl):
    def __init__(self,
                 color_picker: ColorPicker,
                 size_list: ft.Dropdown,
                 color="#000000",
                 tool=DrawingTool()
                 ):
        super().__init__()
        self.tool = tool.LineTool()
        self.state = tool.State()
        self.color = color
        self.color_picker = color_picker
        self.size = 3

        if isinstance(size_list, ft.Dropdown):
            self.size_list = size_list
        else:
            raise ValueError("size_list must be either None or an instance of ft.Dropdown")

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
        # Смена цвет на текущий выбраный цвет в color_picker
        self.color = self.color_picker.color
        # смена размера кисти на выбраный в size_list
        self.size = self.size_list.value

        current_tool = StateDraw.get_instance().current_tool
        if current_tool == "line":
            self.start_x = e.local_x
            self.start_y = e.local_y
        elif current_tool == "rect":
            current_tool_flag = StateFlag.get_instance().current_tool_flag
            self.rectDrawingTool = DrawingTool.RectDrawingTool(canvas=self.holst,
                                                               color=self.color,
                                                               strocke_width=self.size,
                                                               fill_flag=current_tool_flag)
            self.rectDrawingTool.on_pan_start(e)

    def pan_update(self, e: ft.DragUpdateEvent):
        current_tool = StateDraw.get_instance().current_tool
        if current_tool == "line":
            self.tool.draw(
                self.holst,
                start_x=self.start_x,
                start_y=self.start_y,
                end_x=e.local_x,
                end_y=e.local_y,
                color=self.color,
                stroke_width=self.size,
            )
            self.start_x = e.local_x
            self.start_y = e.local_y
        elif current_tool == "rect":
            self.rectDrawingTool.on_pan_update(e)