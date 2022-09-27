import event_handler as eh


class Event:
    def __init__(self, name):
        self.type = name
        self.event_handlers = []

    def add_event_handler(self, event_handler: eh.EventHandler):
        if event_handler in self.event_handlers:
            return
        self.event_handlers.append(event_handler)

    def remove_event_handler(self, event_handler: eh.EventHandler):
        if event_handler in self.event_handlers:
            self.event_handlers.remove(event_handler)

    def notify(self, **kwargs):
        for event_handler in self.event_handlers:
            event_handler.notify(**kwargs)
