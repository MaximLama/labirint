import pyrr
import event_manager as em
import game as gm
import event_handler as eh
import spawnpoint as sp
import model
import math
import collision_projection as cp
import numpy


WORLD_UP = pyrr.Vector3([0., 1., 0.])


class Actor:
    def __init__(self, spawn_point: sp.Spawnpoint = None, model_inst: model.Model = None):

        gm.Game.add_actor(self)
        if spawn_point is None:
            self.position = pyrr.Vector3([0., 0., 0.])
            self.rotation = pyrr.Vector3([0., 0., 0.])
            self.scale = pyrr.Vector3([0., 0., 0.])
        else:
            if spawn_point.position is None:
                self.position = pyrr.Vector3([0., 0., 0.])
            else:
                self.position = spawn_point.position

            if spawn_point.rotation is None:
                self.rotation = pyrr.Vector3([0., 0., 0.])
            else:
                self.rotation = spawn_point.rotation

            if spawn_point.scale is None:
                self.scale = pyrr.Vector3([1., 1., 1.])
            else:
                self.scale = spawn_point.scale

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

        self.translation_matrix = pyrr.Matrix44.from_translation(self.position)
        self.rotation_matrix = pyrr.Matrix44.from_quaternion(pyrr.quaternion.create_from_eulers([
            math.radians(self.rotation[0]),
            math.radians(self.rotation[1]),
            math.radians(self.rotation[2])
        ]))
        self.scale_matrix = pyrr.Matrix44.from_scale(self.scale)
        self.model_matrix = self.translation_matrix*self.rotation_matrix*self.scale_matrix

        if model_inst is None:
            self.model = None
        else:
            self.model = model_inst
            self.collision_projection = cp.CollisionProjection(
                self.model.min_point, self.model.max_point, self.model_matrix)

        self.lights = []

    @classmethod
    def bind(cls, event_name: str, function_name: str):
        ehandler = eh.EventHandler(event_name, cls.__name__, function_name)
        em.EventManager.bind_event_handler(event_name, ehandler)

    def set_position(self, position: pyrr.Vector3):
        self.position = position
        self.translation_matrix = pyrr.Matrix44.from_translation(self.position)
        self.model_matrix = self.translation_matrix * self.rotation_matrix * self.scale_matrix
        if not self.model is None:
            self.collision_projection.change_projection(self.model_matrix)

    def set_rotation(self, rotation: pyrr.Vector3):
        self.rotation = rotation
        self.rotation_matrix = pyrr.Matrix44.from_quaternion(pyrr.quaternion.create_from_eulers([
            math.radians(self.rotation[0]),
            math.radians(self.rotation[1]),
            math.radians(self.rotation[2])
        ]))
        self.model_matrix = self.translation_matrix * self.rotation_matrix * self.scale_matrix
        if not self.model is None:
            self.collision_projection.change_projection(self.model_matrix)

    def set_rotation_from_axis(self, axis: pyrr.Vector4, theta: float):
        self.rotation_matrix = pyrr.Matrix44.from_quaternion(pyrr.Quaternion.from_axis_rotation(axis, theta))
        self.model_matrix = self.translation_matrix * self.rotation_matrix * self.scale_matrix

    def set_scale(self, scale: pyrr.Vector3):
        self.scale = scale
        self.scale_matrix = pyrr.Matrix44.from_scale(self.scale)
        self.model_matrix = self.translation_matrix * self.rotation_matrix * self.scale_matrix
        if not self.model is None:
            self.collision_projection.change_projection(self.model_matrix)

    def get_model_matrix(self):
        return self.model_matrix

    def link_to_actor(self, act):
        pos = act.position
        needed_front = pos - self.position
        needed_front[1] = 0
        pyrr.Vector3.normalize(needed_front)
        angle = pyrr.Vector3.dot(self.front, needed_front)
        if pyrr.Vector3.cross(self.front, needed_front).y > 0:
            self.rotation_matrix = pyrr.Matrix44.from_quaternion(pyrr.Quaternion.from_y_rotation(-math.acos(angle)))
        else:
            self.rotation_matrix = pyrr.Matrix44.from_quaternion(pyrr.Quaternion.from_y_rotation(math.acos(angle)))
        self.model_matrix = self.translation_matrix * self.rotation_matrix * self.scale_matrix
