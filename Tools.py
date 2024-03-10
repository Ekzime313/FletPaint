import flet as ft
import flet.canvas as cv

class State:
    """
       Класс State, который хранит временные данные во время рисования.

       **Атрибуты:**
           x (float): Координата X последнего касания мыши.
           y (float): Координата Y последнего касания мыши.
       """
    x:float
    y:float
class Tool:
    def draw(self, canvas, start_x, start_y, end_x, end_y, **kwargs):
        raise NotImplementedError("Метод рисования не выбран")

class LineTool(Tool):
    def draw(self, canvas,start_x,start_y, end_x,end_y,**kwargs):
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