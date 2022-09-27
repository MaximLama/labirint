import event_manager as em
import game as gm


class EventHandler:
    def __init__(self, event_name: str, class_name: str, function_name: str):
        self.function_name = function_name
        self.event_name = event_name
        self.class_name = class_name
        em.EventManager.bind_event_handler(event_name, self)

    def notify(self, **kwargs):
        actors = gm.Game.get_actors(self.class_name)
        for actor in actors:
            function = getattr(actor, self.function_name, None)
            if callable(function):
                function(**kwargs)

    def __del__(self):
        em.EventManager.unbind_event_handler(self.event_name, self)
