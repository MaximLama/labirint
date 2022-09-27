import pyrr
import math
import actor
import game
import spawnpoint as sp
import physics as ph
import event_manager as em

WORLD_UP = pyrr.Vector3([0., 1., 0.])

FORWARD = 0
BACKWARD = 1
LEFT = 2
RIGHT = 3
UP = 4
DOWN = 5

YAW = -90.
PITCH = 0.
SPEED = 2.5
SENSITIVITY = 0.1
ZOOM = 45.


class Camera(actor.Actor):

    def __init__(self, spawn_point: sp.Spawnpoint):
        super().__init__(spawn_point)
        game.Game.add_actor(self)
        self.movement_speed = SPEED
        self.zoom = ZOOM
        self.mouse_sensitivity = SENSITIVITY
        self.update_camera_vectors()

    def get_view_matrix(self):
        return pyrr.Matrix44.look_at(self.position, self.position + self.front, self.up)

    def process_keyboard(self, direction: float, delta_time: float):
        velocity = self.movement_speed * delta_time
        new_position = None
        if direction == FORWARD:
            new_position = self.position + self.front * velocity
        if direction == BACKWARD:
            new_position = self.position - self.front * velocity
        if direction == LEFT:
            new_position = self.position - self.right * velocity
        if direction == RIGHT:
            new_position = self.position + self.right * velocity
        if direction == UP:
            self.position += WORLD_UP * velocity
        if direction == DOWN:
            self.position -= WORLD_UP * velocity
        new_position.y = 1.178
        if game.Game.show_clsn:
            new_position = ph.Physics.get_new_position(game.Game.level.labirinth_collision, self.position, new_position)
        if ph.Physics.check_intersection([game.Game.level.exit_trigger], self.position, new_position):
            em.EventManager.call("Exit")
        self.set_position(new_position)

    def process_mouse_movement(self, xoffset: float, yoffset: float, constrain_pitch: bool = True):
        xoffset *= self.mouse_sensitivity
        yoffset *= self.mouse_sensitivity

        self.rotation[1] += xoffset
        self.rotation[2] += yoffset

        if constrain_pitch:
            if self.rotation[2] > 89.:
                self.rotation[2] = 89.
            if self.rotation[2] < -89.:
                self.rotation[2] = -89.

        self.update_camera_vectors()

    def process_mouse_scroll(self, yoffset: float):
        if (self.zoom >= 1.) and (self.zoom <= 45.):
            self.zoom -= yoffset
        if self.zoom <= 1.:
            self.zoom = 1.
        if self.zoom >= 45.:
            self.zoom = 45

    def update_camera_vectors(self):
        self.front = pyrr.Vector3([
            math.cos(math.radians(self.rotation[1])) * math.cos(math.radians(self.rotation[2])),
            math.sin(math.radians(self.rotation[2])),
            math.sin(math.radians(self.rotation[1])) * math.cos(math.radians(self.rotation[2])),
        ])
        pyrr.Vector3.normalize(self.front)
        self.right = pyrr.Vector3.cross(self.front, WORLD_UP)
        pyrr.Vector3.normalize(self.right)
        self.up = pyrr.Vector3.cross(self.right, self.front)
        pyrr.Vector3.normalize(self.up)