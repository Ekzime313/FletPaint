import flet as ft
import flet.canvas as cv
import math

class DrawingTool:
    class State:
        x: float
        y: float

    class Tool:
        def draw(self, canvas, start_x, start_y, end_x, end_y, **kwargs):
            raise NotImplementedError("Метод рисования не выбран")

    class LineTool(Tool):
        def draw(self, canvas, start_x, start_y, end_x, end_y, **kwargs):
            canvas.shapes.append(
                cv.Line(
                    start_x,
                    start_y,
                    end_x,
                    end_y,
                    paint=ft.Paint(
                        color=kwargs["color"],
                        stroke_width=kwargs['stroke_width']
                    )
                )
            )
            canvas.update()

    class RectDrawingTool:
        def __init__(self, canvas: cv.Canvas,
                     color:ft.colors,
                     stroke_width = 2,
                     fill_flag = False):
            self.canvas = canvas
            self.color = color
            self.size = stroke_width
            self.fill_flag = fill_flag
            self.rect_start_point = None
            self.current_rect = None

        def on_pan_start(self, e: ft.DragStartEvent):
            if self.fill_flag:
                self.paint = ft.Paint(color=self.color, stroke_width=self.size)
            else:
                self.paint = ft.Paint(color=self.color, stroke_width=self.size, style=ft.PaintingStyle.STROKE)
            self.rect_start_point = (e.local_x, e.local_y)
            self.current_rect = cv.Rect(
                x=self.rect_start_point[0],
                y=self.rect_start_point[1],
                width=0,
                height=0,
                paint=self.paint
            )
            self.canvas.shapes.append(self.current_rect)
            self.canvas.update()

        def on_pan_update(self, e: ft.DragUpdateEvent):
            if self.current_rect:
                width = e.local_x - self.rect_start_point[0]
                height = e.local_y - self.rect_start_point[1]
                self.current_rect.width = width
                self.current_rect.height = height
                self.canvas.update()

        def on_pan_end(self, e: ft.DragEndEvent):
            self.rect_start_point = None
            self.current_rect = None

    class CircleDrawTool:
        def __init__(self, canvas: cv.Canvas,
                     color: ft.colors,
                     stroke_width=2,
                     fill_flag=False):
            self.canvas = canvas
            self.color = color
            self.size = stroke_width
            self.fill_flag = fill_flag
            self.circle_start_point = None
            self.current_circle = None

        def on_pan_start(self, e: ft.DragStartEvent):
            if self.fill_flag:
                self.paint = ft.Paint(color=self.color, stroke_width=self.size)
            else:
                self.paint = ft.Paint(color=self.color, stroke_width=self.size, style=ft.PaintingStyle.STROKE)
            self.circle_start_point = (e.local_x, e.local_y)
            self.current_circle = cv.Circle(
                x=self.circle_start_point[0],
                y=self.circle_start_point[1],
                radius=0,
                paint=self.paint
            )
            self.canvas.shapes.append(self.current_circle)
            self.canvas.update()

        def on_pan_update(self, e: ft.DragUpdateEvent):
            if self.current_circle:
                radius = math.sqrt((e.local_x - self.current_circle.x) ** 2 + (e.local_y - self.current_circle.y) ** 2)
                self.current_circle.radius = radius
                self.canvas.update()

        def on_pan_end(self, e: ft.DragEndEvent):
            self.circle_start_point = None
            self.current_circle = None