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
    """
       Базовый класс для инструментов рисования.

       **Методы:**
           draw(self, canvas, start_x, start_y, end_x, end_y, **kwargs):
               Абстрактный метод, который должен быть реализован в подклассах
               для конкретной логики рисования фигуры.

       **Ошибки:**
           NotImplementedError: Возникает, если метод draw не реализован в подклассе.
       """
    def draw(self, canvas, start_x, start_y, end_x, end_y, **kwargs):
        raise NotImplementedError("Метод рисования не выбран")

class LineTool(Tool):
    """
        Класс LineTool - инструмент рисования линий.

        **Методы:**
            draw(self, canvas, start_x, start_y, end_x, end_y, **kwargs):
                Метод отрисовки линии на холсте.

        **Аргументы:**
            canvas (cv.Canvas): Холст для рисования.
            start_x (float): Начальная координата X по оси X.
            start_y (float): Начальная координата Y по оси Y.
            end_x (float): Конечная координата X по оси X.
            end_y (float): Конечная координата Y по оси Y.
            **kwargs: Словарь дополнительных параметров (например, толщина линии).
        """
    def draw(self, canvas,start_x,start_y, end_x,end_y,**kwargs):
        """
                Отрисовывает линию на холсте.

                1. Создает объект cv.Line с начальными и конечными координатами, толщиной линии.
                2. Добавляет линию в список фигур холста (canvas.shapes).
                3. Обновляет холст (canvas.update).
                """
        canvas.shapes.append(
            cv.Line(
                start_x,
                start_y,
                end_x,
                end_y,
                paint=ft.Paint(
                    color=kwargs["color"],
                    stroke_width=3
                )
            )
        )
        canvas.update()