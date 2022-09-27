import actor
import spawnpoint as sp
import camera


class Character(actor.Actor):
    def __init__(self, spawn_point: sp.Spawnpoint):
        super().__init__(spawn_point)
        self.camera = camera.Camera(spawn_point)
        self.bind("MouseMove", "mouse_move_camera")

    def mouse_move_camera(self, x_offset, y_offset):
        self.camera.process_mouse_movement(x_offset, y_offset)

    def key_move_camera(self, **params):
        self.camera.process_keyboard(**params)