class StateDraw:
    __instance = None

    @staticmethod
    def get_instance():
        if StateDraw.__instance is None:
            StateDraw.__instance = StateDraw()
        return StateDraw.__instance

    def __init__(self):
        self.current_tool = "line"

class StateFlag:
    __instance = None

    @staticmethod
    def get_instance():
        if StateFlag.__instance is None:
            StateFlag.__instance = StateFlag()
        return StateFlag.__instance

    def __init__(self):
        self.current_tool_flag =  False