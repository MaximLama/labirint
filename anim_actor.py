import actor
import game
import spawnpoint as sp
import model
import sprite_animator as sa
from OpenGL.GL import *


class AnimActor(actor.Actor):
    def __init__(self, spawn_point: sp.Spawnpoint = None, model_inst: model.Model = None):
        super().__init__(spawn_point, model_inst)
        self.animator = None

    def create_sprite_animator(self, rows, columns, time = 1):
        self.animator = sa.SpriteAnimator(rows, columns, time)
        self.sprite_anim_update()

    def sprite_anim_update(self):
        X = 0
        Y = 1

        V0 = 3
        V1 = 11
        V2 = 19
        V3 = 27

        frame_width = 1. / self.animator.columns
        frame_height = 1. / self.animator.rows

        row = self.animator.current_frame // self.animator.columns
        col = self.animator.current_frame % self.animator.columns

        for i in range(len(self.model.meshes)):
            self.model.meshes[i].vertices[V0 + X] = frame_width * col
            self.model.meshes[i].vertices[V0 + Y] = frame_height * (row + 1)
            self.model.meshes[i].vertices[V1 + X] = frame_width * col
            self.model.meshes[i].vertices[V1 + Y] = frame_height * row
            self.model.meshes[i].vertices[V2 + X] = frame_width * (col + 1)
            self.model.meshes[i].vertices[V2 + Y] = frame_height * (row + 1)
            self.model.meshes[i].vertices[V3 + X] = frame_width * (col + 1)
            self.model.meshes[i].vertices[V3 + Y] = frame_height * row

            glBindBuffer(GL_ARRAY_BUFFER, self.model.meshes[i].VBO)
            glBufferData(GL_ARRAY_BUFFER, len(self.model.meshes[i].vertices) * 4, self.model.meshes[i].vertices, GL_DYNAMIC_DRAW)

    def sprite_anim_next_frame(self):
        if self.animator.time_frame > self.animator.time/(self.animator.rows*self.animator.columns):
            self.animator.time_frame = 0
            max_frame = self.animator.columns * self.animator.rows - 1
            if max_frame == self.animator.current_frame:
                self.animator.current_frame = 0
            else:
                self.animator.current_frame += 1
            self.sprite_anim_update()
        else:
            self.animator.time_frame += game.Game.delta_time
