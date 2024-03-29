import flet as ft
from current_draw_tool import StateDraw, StateFlag
class SwitchShape(ft.UserControl):
    def build(self):
        self.line = ft.Row(
            controls=[
                ft.Icon(ft.icons.LINEAR_SCALE),
                ft.CupertinoSwitch(
                    label="Draw line",
                    value=True,
                    on_change=self.line_on
                )
            ]
        )
        self.rect = ft.Row(
            controls=[
                ft.Icon(ft.icons.RECTANGLE),
                ft.CupertinoSwitch(
                    label="Draw Rect",
                    value=False,
                    on_change=self.rect_on
                )
            ]
        )
        self.circle = ft.Row(
            controls=[
                ft.Icon(ft.icons.CIRCLE),
                ft.CupertinoSwitch(
                    label="Draw Circle",
                    value=False,
                    on_change=self.circle_on
                )
            ]
        )
        self.flag_fill = ft.Checkbox(
            label="fill",
            value=False,
            visible=False,
            on_change=self.flag_on
        )
        view = ft.Column(
            controls=[
                self.line,
                self.rect,
                self.circle,
                self.flag_fill
            ]
        )
        return view
    def line_on(self,e):
        line_switch = self.line.controls[1]
        rect_switch = self.rect.controls[1]
        circle_switch = self.circle.controls[1]

        if e.control is line_switch:
            circle_switch.value = False
            rect_switch.value = False
            self.flag_fill.value = False
            self.flag_fill.visible = False
            self.update()
        else:
            line_switch.value = False
            self.update()
        state = StateDraw.get_instance()
        state.current_tool = "line"
    def rect_on(self, e):
        line_switch = self.line.controls[1]
        rect_switch = self.rect.controls[1]
        circle_switch = self.circle.controls[1]

        if e.control is rect_switch:
            circle_switch.value = False
            line_switch.value = False
            self.flag_fill.visible = True
            self.update()
        else:
            rect_switch.value = False
            self.update()
        state = StateDraw.get_instance()
        state.current_tool = "rect"

    def circle_on(self, e):
        line_switch = self.line.controls[1]
        rect_switch = self.rect.controls[1]
        circle_switch = self.circle.controls[1]

        if e.control is circle_switch:
            rect_switch.value = False
            line_switch.value = False
            self.flag_fill.visible = True
            self.update()
        else:
            circle_switch.value = False
            self.update()
        state = StateDraw.get_instance()
        state.current_tool = "circle"

    def flag_on(self,e):
        state = StateFlag().get_instance()
        state.current_tool_flag = self.flag_fill.value