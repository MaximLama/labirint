import glfw
import pyrr
import window as win
from OpenGL.GL import *
import character as ch
import spawnpoint as sp
import key_input_controller as kic
import camera
import level as lvl

class Game:

    # params:
    # WIDTH_SCR - ширина окна
    # HEIGHT_SCR - высота окна
    # WINDOW_NAME - имя окна

    __instance = None
    actors = []
    character = None
    main_window = None
    models = []
    shaders = {}
    show_clsn = True
    level = None
    delta_time = 0

    def __new__(cls):
        if not hasattr(cls, '__instance'):
            cls.__instance = super(Game, cls).__new__(cls)
        return cls.__instance

    def __init__(self):
        self.params = self.load_game_properties()
        self.last_frame = 0.

    def initialize(self):
        Game.main_window = win.Window(
            self.params["WINDOW_NAME"]
        )
        Game.add_actor(self.main_window)
        Game.character = ch.Character(sp.Spawnpoint(
            pyrr.Vector3([16.5, 1.178, 1.8]),
            pyrr.Vector3([0., -90., 0.]),
            pyrr.Vector3([1., 1., 1.])
        ))
        self.create_input_events()
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_CULL_FACE)
        glFrontFace(GL_CCW)
        #Game.turn_out_collision()
        Game.level = lvl.Level("Main")

    def update(self):
        while not glfw.window_should_close(Game.main_window.window):
            self.current_frame = glfw.get_time()
            Game.delta_time = self.current_frame - self.last_frame
            self.last_frame = self.current_frame
            kic.KeyInputController.update_data("delta_time", Game.delta_time)
            kic.KeyInputController.call_input_events(Game.main_window.window)
            glClearColor(0.1, 0.1, 0.1, 1.0)
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            Game.level.draw()

            glfw.swap_buffers(Game.main_window.window)
            glfw.poll_events()

    @staticmethod
    def load_game_properties():
        params = {}
        with open("files/game_properties.txt") as f:
            lines = f.readlines()
            for line in lines:
                parameter = line.split(":")
                parameter_name = parameter[0].strip()
                params[parameter_name] = parameter[1].strip()
        return params

    @classmethod
    def get_actors(cls, class_name: str = None):
        if class_name is None:
            return cls.actors
        else:
            ls = []
            for actor_inst in cls.actors:
                if actor_inst.__class__.__name__ == class_name:
                    ls.append(actor_inst)
            return ls

    @classmethod
    def add_actor(cls, actor_inst):
        if actor_inst:
            if actor_inst in cls.actors:
                return
            cls.actors.append(actor_inst)

    def create_input_events(self):
        kic.KeyInputController.add_key_handlers(
            glfw.KEY_W,
            "Forward",
            "Character",
            "key_move_camera",
            direction=camera.FORWARD,
            delta_time=Game.delta_time
        )
        kic.KeyInputController.add_key_handlers(
            glfw.KEY_A,
            "Left",
            "Character",
            "key_move_camera",
            direction=camera.LEFT,
            delta_time=Game.delta_time
        )
        kic.KeyInputController.add_key_handlers(
            glfw.KEY_S,
            "Backward",
            "Character",
            "key_move_camera",
            direction=camera.BACKWARD,
            delta_time=Game.delta_time
        )
        kic.KeyInputController.add_key_handlers(
            glfw.KEY_D,
            "Right",
            "Character",
            "key_move_camera",
            direction=camera.RIGHT,
            delta_time=Game.delta_time
        )
        kic.KeyInputController.add_key_handlers(
            glfw.KEY_ESCAPE,
            "Exit",
            "Window",
            "close_window"
        )

    @classmethod
    def turn_out_collision(cls):
        Game.show_clsn = False