import event
import event_handler as eh


class EventManager:

    events = {}

    @classmethod
    def add_event(cls, e: event.Event):
        if e.type in cls.events:
            return
        cls.events[e.type] = e

    @classmethod
    def remove_event(cls, name: str):
        if name in cls.events:
            del cls.events[name]

    @classmethod
    def bind_event_handler(cls, event_name: str, event_handler: eh.EventHandler):
        if event_name in cls.events:
            cls.events[event_name].add_event_handler(event_handler)

    @classmethod
    def unbind_event_handler(cls, event_name: str, event_handler: eh.EventHandler):
        if event_name in cls.events:
            cls.events[event_name].remove_event_handler(event_handler)

    @classmethod
    def call(cls, event_name: str, **kwargs):
        if event_name in cls.events:
            cls.events[event_name].notify(**kwargs)
