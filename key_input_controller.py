import input_controller as ic
import event_handler as eh
import event_manager as em
import event
import glfw


class KeyInputController(ic.InputController):
    __instance = None
    key_events = {}

    def __new__(cls):
        if not hasattr(cls, '__instance'):
            cls.__instance = super(KeyInputController, cls).__new__(cls)
        return cls.__instance

    def __init__(self):
        ic.InputController.__init__(self)

    @classmethod
    def add_key_handlers(cls, key: int, event_name, class_name, function_name, **function_params):
        em.EventManager.add_event(event.Event(event_name))
        cls.key_events[key] = {'event':event_name, 'params':function_params}
        em.EventManager.bind_event_handler(event_name, eh.EventHandler(event_name, class_name, function_name))

    @classmethod
    def call_input_events(cls, window):
        for key, value in cls.key_events.items():
            if glfw.get_key(window, key) == glfw.PRESS:
                em.EventManager.call(cls.key_events[key]["event"], **cls.key_events[key]["params"])

    @classmethod
    def update_data(cls, param, value):
        for key in cls.key_events:
            if param in cls.key_events[key]["params"]:
                cls.key_events[key]["params"][param] = value
