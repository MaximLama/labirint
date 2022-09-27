import input_controller as ic
import event_manager as em
import event


class MouseInputController(ic.InputController):
    __instance = None

    def __new__(cls):
        if not hasattr(cls, '__instance'):
            cls.__instance = super(MouseInputController, cls).__new__(cls)
        return cls.__instance

    def __init__(self):
        ic.InputController.__init__(self)
        self.firstMouse = True
        self.lastX = None
        self.lastY = None
        self.x_offset = None
        self.y_offset = None
        MouseInputController.create_events()

    @staticmethod
    def create_events():
        em.EventManager.add_event(event.Event("MouseMove"))

    # Функция управления мышью
    def mouse_callback(self, window, xpos, ypos):
        if self.firstMouse:
            self.lastX = xpos
            self.lastY = ypos
            self.firstMouse = False

        self.x_offset = xpos - self.lastX
        self.y_offset = self.lastY - ypos

        self.lastX = xpos
        self.lastY = ypos
        em.EventManager.call("MouseMove", x_offset=self.x_offset, y_offset=self.y_offset)