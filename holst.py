import flet as ft
import flet.canvas as cv
from Tools import LineTool, State

class Holst(ft.UserControl):
    """
        Класс Holst, который представляет собой холст для рисования.

        **Атрибуты:**
            tool: Экземпляр класса Tool, который является инструментом рисования (по умолчанию LineTool).
            state: Экземпляр класса State, который хранит временные данные рисования.
        """
    def __init__(self, tool=LineTool()):
        """
                Конструктор класса Holst.

                Args:
                    tool:  (Optional) Экземпляр класса Tool. По умолчанию используется LineTool.
                """
        super().__init__()
        self.tool = tool
        self.state = State()

    def build(self):
        """
                Метод build, который строит и возвращает холст для рисования.

                **Возвращает:**
                    Экземпляр класса cv.Canvas, который представляет собой холст для рисования.
                """
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
        """
                Обработчик события pan_start, который сохраняет начальные координаты касания.

                Args:
                    e: Экземпляр класса ft.DragStartEvent, который содержит информацию о начале события перемещения.
                """
        self.state.x = e.local_x
        self.state.y = e.local_y

    def pan_update(self, e: ft.DragUpdateEvent):
        """
               Обработчик события pan_update, который вызывает метод draw инструмента рисования
               и обновляет координаты касания.

               Args:
                   e: Экземпляр класса ft.DragUpdateEvent, который содержит информацию о текущем положении касания.
               """
        self.tool.draw(
            self.holst,
            start_x=self.state.x,
            start_y=self.state.y,
            end_x=e.local_x,
            end_y=e.local_y,
            stroke_width=3
        )
        self.state.x = e.local_x
        self.state.y = e.local_y