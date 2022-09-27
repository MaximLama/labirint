import actor
import model
import shader as sh
import game
import pyrr
import spawnpoint as sp
import numpy
from OpenGL.GL import *
import anim_actor as aa


class Level:
    def __init__(self, name):
        self.labirinth_collision = []
        self.exit_trigger = None
        self.illuminated_objects = []
        self.illuminated = []
        self.name = name
        self.walls = []
        self.wall_model = None
        self.wall_corner_out = []
        self.wall_corner_out_model = None
        self.floor_model = None
        self.floors = []
        self.floor_rectangle_model = None
        self.floor_rectangles = []
        self.torch_model = None
        self.torches = []
        self.fire_model = None
        self.fires = []
        self.exit_sprite_model = None
        self.exit_sprites = []
        self.mem_model = None
        self.mems = []
        self.skybox_model = None
        self.skyboxes = []
        self.create_shaders()
        self.load_skybox()
        self.load_walls()
        self.load_wall_corner_out()
        self.load_floors()
        self.load_floor_rectangles()
        self.load_torches()
        self.load_fires()
        self.load_exit_sprite()
        self.load_mem()
        self.load_exit_trigger()
        #self.build_lights()
        #self.prepare_walls()
        #print(game.Game.shaders)

    def create_shaders(self):
        sh.Shader("shaders/rock.vs", "shaders/rock.fs", "ads")
        sh.Shader("shaders/rock.vs", "shaders/alpha.fs", "fire")

    def load_skybox(self):
        self.skybox_model = model.Model("resources/skybox/skybox.obj",
                                      "resources/skybox/skybox.mtl")
        self.skybox_coords = numpy.array([
            [pyrr.Vector3([0., 0, 0]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([60, 60, 60])]
        ])
        for coords in self.skybox_coords:
            new_actor = actor.Actor(
                sp.Spawnpoint(*coords), self.skybox_model
            )
            self.skyboxes.append(
                new_actor
            )
        model_identity = pyrr.Matrix44.identity()
        model_matrices = list()
        for skybox in self.skyboxes:
            model_inst = model_identity * skybox.get_model_matrix()
            model_matrices.append(model_inst)
        model_matrices = numpy.array(model_matrices, dtype=numpy.float32)

        self.skybox_model.prepare_instanced_draw(model_matrices)

    def load_walls(self):
        self.wall_model = model.Model("resources/wall/Wall.obj", "resources/wall/Wall.mtl")
        self.wall_coords = numpy.array([
            # 0

            # 17
            [pyrr.Vector3([17., 0., 2.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1., 1.5, 1.])],

            # 1

            # 2
            [pyrr.Vector3([2., 0., 1.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 3
            [pyrr.Vector3([3., 0., 1.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 4
            [pyrr.Vector3([4., 0., 1.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 5
            [pyrr.Vector3([5., 0., 1.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 6
            [pyrr.Vector3([6., 0., 1.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 7
            [pyrr.Vector3([7., 0., 1.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 8
            [pyrr.Vector3([8., 0., 1.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 9
            [pyrr.Vector3([9., 0., 1.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 10
            [pyrr.Vector3([10., 0., 1.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 11
            [pyrr.Vector3([11., 0., 1.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 12
            [pyrr.Vector3([12., 0., 1.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 13
            [pyrr.Vector3([13., 0., 1.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 14
            [pyrr.Vector3([14., 0., 1.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 15
            [pyrr.Vector3([15., 0., 1.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 18
            [pyrr.Vector3([17., 0., 1.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 20
            [pyrr.Vector3([20., 0., 1.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 21
            [pyrr.Vector3([21., 0., 1.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 22
            [pyrr.Vector3([22., 0., 1.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 23
            [pyrr.Vector3([23., 0., 1.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 24
            [pyrr.Vector3([24., 0., 1.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 25
            [pyrr.Vector3([25., 0., 1.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 26
            [pyrr.Vector3([26., 0., 1.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 27
            [pyrr.Vector3([27., 0., 1.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 28
            [pyrr.Vector3([28., 0., 1.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 29
            [pyrr.Vector3([29., 0., 1.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1., 1.5, 1.])],

            # 2

            # 1
            [pyrr.Vector3([1., 0., 1.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 18
            [pyrr.Vector3([17., 0., 0.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 19
            [pyrr.Vector3([19., 0., 1.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 30
            [pyrr.Vector3([29., 0., 0.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],

            # 3

            # 1
            [pyrr.Vector3([1., 0., 0.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 4
            [pyrr.Vector3([3., 0., 0.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 5
            [pyrr.Vector3([4., 0., 0.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 6
            [pyrr.Vector3([5., 0., 0.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 13
            [pyrr.Vector3([12., 0., 0.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 14
            [pyrr.Vector3([13., 0., 0.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 15
            [pyrr.Vector3([14., 0., 0.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 18
            [pyrr.Vector3([17., 0., -1.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 19
            [pyrr.Vector3([19., 0., 0.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 25
            [pyrr.Vector3([24., 0., 0.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 26
            [pyrr.Vector3([25., 0., 0.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 27
            [pyrr.Vector3([26., 0., 0.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 30
            [pyrr.Vector3([29., 0., -1.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],

            # 4

            # 1
            [pyrr.Vector3([1., 0., -1.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 3
            [pyrr.Vector3([2., 0., -2.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 5
            [pyrr.Vector3([5., 0., -2.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 6
            [pyrr.Vector3([6., 0., -2.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 9
            [pyrr.Vector3([8., 0., -2.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 10
            [pyrr.Vector3([10., 0., -1.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 13
            [pyrr.Vector3([13., 0., -2.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 14
            [pyrr.Vector3([14., 0., -2.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 16
            [pyrr.Vector3([16., 0., -1.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 21
            [pyrr.Vector3([20., 0., -2.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 22
            [pyrr.Vector3([22., 0., -1.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 24
            [pyrr.Vector3([23., 0., -2.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 26
            [pyrr.Vector3([26., 0., -2.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 27
            [pyrr.Vector3([27., 0., -2.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 30
            [pyrr.Vector3([29., 0., -2.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],

            # 5

            # 1
            [pyrr.Vector3([1., 0., -2.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 3
            [pyrr.Vector3([2., 0., -3.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 4
            [pyrr.Vector3([4., 0., -2.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 9
            [pyrr.Vector3([8., 0., -3.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 10
            [pyrr.Vector3([10., 0., -2.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 15
            [pyrr.Vector3([14., 0., -3.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 16
            [pyrr.Vector3([16., 0., -2.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 21
            [pyrr.Vector3([20., 0., -3.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 22
            [pyrr.Vector3([22., 0., -2.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 24
            [pyrr.Vector3([23., 0., -3.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 25
            [pyrr.Vector3([25., 0., -2.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 30
            [pyrr.Vector3([29., 0., -3.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],

            # 6

            # 1
            [pyrr.Vector3([1., 0., -3.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 3
            [pyrr.Vector3([2., 0., -4.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 5
            [pyrr.Vector3([4., 0., -3.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 6
            [pyrr.Vector3([5., 0., -3.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 9
            [pyrr.Vector3([8., 0., -4.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 11
            [pyrr.Vector3([10., 0., -3.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 12
            [pyrr.Vector3([11., 0., -3.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 13
            [pyrr.Vector3([12., 0., -3.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 14
            [pyrr.Vector3([13., 0., -3.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 17
            [pyrr.Vector3([16., 0., -3.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 18
            [pyrr.Vector3([17., 0., -3.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 19
            [pyrr.Vector3([18., 0., -3.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 20
            [pyrr.Vector3([19., 0., -3.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 23
            [pyrr.Vector3([22., 0., -3.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 25
            [pyrr.Vector3([25., 0., -3.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 28
            [pyrr.Vector3([27., 0., -3.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 29
            [pyrr.Vector3([28., 0., -3.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1., 1.5, 1.])],

            # 7

            # 1
            [pyrr.Vector3([1., 0., -4.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 4
            [pyrr.Vector3([4., 0., -5.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 5
            [pyrr.Vector3([5., 0., -5.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 7
            [pyrr.Vector3([7., 0., -4.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 10
            [pyrr.Vector3([10., 0., -5.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 11
            [pyrr.Vector3([11., 0., -5.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 14
            [pyrr.Vector3([14., 0., -5.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 15
            [pyrr.Vector3([15., 0., -5.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 16
            [pyrr.Vector3([16., 0., -5.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 17
            [pyrr.Vector3([17., 0., -5.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 20
            [pyrr.Vector3([20., 0., -5.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 23
            [pyrr.Vector3([23., 0., -5.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 24
            [pyrr.Vector3([24., 0., -5.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 28
            [pyrr.Vector3([28., 0., -5.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 29
            [pyrr.Vector3([29., 0., -5.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1., 1.5, 1.])],

            # 8

            # 1
            [pyrr.Vector3([1., 0., -5.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 6
            [pyrr.Vector3([5., 0., -6.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 7
            [pyrr.Vector3([7., 0., -5.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 12
            [pyrr.Vector3([11., 0., -6.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 13
            [pyrr.Vector3([13., 0., -5.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 18
            [pyrr.Vector3([17., 0., -6.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 19
            [pyrr.Vector3([19., 0., -5.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 21
            [pyrr.Vector3([20., 0., -6.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 22
            [pyrr.Vector3([22., 0., -5.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 30
            [pyrr.Vector3([29., 0., -6.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],

            # 9

            # 1
            [pyrr.Vector3([1., 0., -6.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 6
            [pyrr.Vector3([5., 0., -7.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 8
            [pyrr.Vector3([7., 0., -6.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 9
            [pyrr.Vector3([8., 0., -6.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 10
            [pyrr.Vector3([9., 0., -6.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 11
            [pyrr.Vector3([10., 0., -6.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 13
            [pyrr.Vector3([13., 0., -6.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 16
            [pyrr.Vector3([15., 0., -6.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 17
            [pyrr.Vector3([16., 0., -6.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 19
            [pyrr.Vector3([19., 0., -6.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 21
            [pyrr.Vector3([20., 0., -7.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 23
            [pyrr.Vector3([22., 0., -6.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 24
            [pyrr.Vector3([23., 0., -6.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 25
            [pyrr.Vector3([24., 0., -6.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 26
            [pyrr.Vector3([25., 0., -6.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 27
            [pyrr.Vector3([26., 0., -6.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 30
            [pyrr.Vector3([29., 0., -7.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],

            # 10

            # 1
            [pyrr.Vector3([1., 0., -7.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 3
            [pyrr.Vector3([2., 0., -8.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 4
            [pyrr.Vector3([4., 0., -7.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 6
            [pyrr.Vector3([5., 0., -8.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 8
            [pyrr.Vector3([8., 0., -8.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 9
            [pyrr.Vector3([9., 0., -8.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 10
            [pyrr.Vector3([10., 0., -8.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 11
            [pyrr.Vector3([11., 0., -8.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 13
            [pyrr.Vector3([13., 0., -7.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 15
            [pyrr.Vector3([14., 0., -8.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 17
            [pyrr.Vector3([17., 0., -8.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 18
            [pyrr.Vector3([18., 0., -8.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 21
            [pyrr.Vector3([20., 0., -8.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 23
            [pyrr.Vector3([23., 0., -8.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 24
            [pyrr.Vector3([24., 0., -8.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 25
            [pyrr.Vector3([25., 0., -8.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 26
            [pyrr.Vector3([26., 0., -8.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 27
            [pyrr.Vector3([27., 0., -8.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 30
            [pyrr.Vector3([29., 0., -8.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],

            # 11

            # 1
            [pyrr.Vector3([1., 0., -8.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 3
            [pyrr.Vector3([2., 0., -9.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 4
            [pyrr.Vector3([4., 0., -8.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 6
            [pyrr.Vector3([5., 0., -9.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 7
            [pyrr.Vector3([7., 0., -8.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 12
            [pyrr.Vector3([11., 0., -9.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 13
            [pyrr.Vector3([13., 0., -8.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 15
            [pyrr.Vector3([14., 0., -9.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 16
            [pyrr.Vector3([16., 0., -8.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 21
            [pyrr.Vector3([20., 0., -9.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 22
            [pyrr.Vector3([22., 0., -8.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 30
            [pyrr.Vector3([29., 0., -9.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],

            # 12

            # 2
            [pyrr.Vector3([1., 0., -9.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 4
            [pyrr.Vector3([4., 0., -9.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 6
            [pyrr.Vector3([5., 0., -10.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 8
            [pyrr.Vector3([7., 0., -9.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 9
            [pyrr.Vector3([8., 0., -9.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 12
            [pyrr.Vector3([11., 0., -10.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 13
            [pyrr.Vector3([13., 0., -9.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 15
            [pyrr.Vector3([14., 0., -10.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 16
            [pyrr.Vector3([16., 0., -9.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 19
            [pyrr.Vector3([18., 0., -9.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 20
            [pyrr.Vector3([19., 0., -9.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 23
            [pyrr.Vector3([22., 0., -9.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 24
            [pyrr.Vector3([23., 0., -9.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 30
            [pyrr.Vector3([29., 0., -10.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],

            # 13

            # 2
            [pyrr.Vector3([2., 0., -11.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 3
            [pyrr.Vector3([3., 0., -11.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 6
            [pyrr.Vector3([5., 0., -11.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 8
            [pyrr.Vector3([8., 0., -11.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 9
            [pyrr.Vector3([9., 0., -11.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 15
            [pyrr.Vector3([14., 0., -11.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 16
            [pyrr.Vector3([16., 0., -10.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 18
            [pyrr.Vector3([17., 0., -11.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 20
            [pyrr.Vector3([20., 0., -11.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 21
            [pyrr.Vector3([21., 0., -11.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 22
            [pyrr.Vector3([22., 0., -11.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 23
            [pyrr.Vector3([23., 0., -11.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 24
            [pyrr.Vector3([24., 0., -11.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 27
            [pyrr.Vector3([26., 0., -11.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 28
            [pyrr.Vector3([28., 0., -10.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 30
            [pyrr.Vector3([29., 0., -11.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],

            # 14

            # 1
            [pyrr.Vector3([1., 0., -11.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 6
            [pyrr.Vector3([5., 0., -12.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 7
            [pyrr.Vector3([7., 0., -11.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 15
            [pyrr.Vector3([14., 0., -12.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 16
            [pyrr.Vector3([16., 0., -11.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 18
            [pyrr.Vector3([17., 0., -12.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 19
            [pyrr.Vector3([19., 0., -11.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 27
            [pyrr.Vector3([26., 0., -12.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 28
            [pyrr.Vector3([28., 0., -11.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 30
            [pyrr.Vector3([29., 0., -12.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],

            # 15

            # 1
            [pyrr.Vector3([1., 0., -12.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 4
            [pyrr.Vector3([3., 0., -12.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 5
            [pyrr.Vector3([4., 0., -12.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 7
            [pyrr.Vector3([7., 0., -12.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 10
            [pyrr.Vector3([9., 0., -12.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 11
            [pyrr.Vector3([10., 0., -12.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 12
            [pyrr.Vector3([11., 0., -12.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 13
            [pyrr.Vector3([12., 0., -12.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 14
            [pyrr.Vector3([13., 0., -12.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 16
            [pyrr.Vector3([16., 0., -12.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 18
            [pyrr.Vector3([17., 0., -13.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 19
            [pyrr.Vector3([19., 0., -12.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 22
            [pyrr.Vector3([21., 0., -12.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 23
            [pyrr.Vector3([22., 0., -12.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 24
            [pyrr.Vector3([23., 0., -12.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 25
            [pyrr.Vector3([24., 0., -12.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 26
            [pyrr.Vector3([25., 0., -12.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 28
            [pyrr.Vector3([28., 0., -12.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 30
            [pyrr.Vector3([29., 0., -13.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],

            # 16

            # 1
            [pyrr.Vector3([1., 0., -13.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 3
            [pyrr.Vector3([2., 0., -14.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 5
            [pyrr.Vector3([5., 0., -14.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 7
            [pyrr.Vector3([7., 0., -13.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 10
            [pyrr.Vector3([10., 0., -14.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 11
            [pyrr.Vector3([11., 0., -14.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 12
            [pyrr.Vector3([12., 0., -14.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 13
            [pyrr.Vector3([13., 0., -14.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 14
            [pyrr.Vector3([14., 0., -14.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 16
            [pyrr.Vector3([16., 0., -13.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 18
            [pyrr.Vector3([17., 0., -14.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 19
            [pyrr.Vector3([19., 0., -13.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 22
            [pyrr.Vector3([22., 0., -14.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 23
            [pyrr.Vector3([23., 0., -14.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 24
            [pyrr.Vector3([24., 0., -14.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 25
            [pyrr.Vector3([25., 0., -14.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 26
            [pyrr.Vector3([26., 0., -14.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 28
            [pyrr.Vector3([28., 0., -13.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 30
            [pyrr.Vector3([29., 0., -14.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],

            # 17

            # 1
            [pyrr.Vector3([1., 0., -14.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 3
            [pyrr.Vector3([2., 0., -15.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 4
            [pyrr.Vector3([4., 0., -14.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 6
            [pyrr.Vector3([5., 0., -15.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 7
            [pyrr.Vector3([7., 0., -14.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 15
            [pyrr.Vector3([14., 0., -15.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 16
            [pyrr.Vector3([16., 0., -14.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 18
            [pyrr.Vector3([17., 0., -15.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 19
            [pyrr.Vector3([19., 0., -14.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 27
            [pyrr.Vector3([26., 0., -15.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 28
            [pyrr.Vector3([28., 0., -14.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 30
            [pyrr.Vector3([29., 0., -15.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],

            # 18

            # 1
            [pyrr.Vector3([1., 0., -15.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 3
            [pyrr.Vector3([2., 0., -16.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 4
            [pyrr.Vector3([4., 0., -15.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 6
            [pyrr.Vector3([5., 0., -16.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 7
            [pyrr.Vector3([7., 0., -15.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 10
            [pyrr.Vector3([9., 0., -15.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 11
            [pyrr.Vector3([10., 0., -15.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 12
            [pyrr.Vector3([11., 0., -15.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 15
            [pyrr.Vector3([14., 0., -16.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 16
            [pyrr.Vector3([16., 0., -15.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 18
            [pyrr.Vector3([17., 0., -16.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 20
            [pyrr.Vector3([19., 0., -15.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 21
            [pyrr.Vector3([20., 0., -15.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 22
            [pyrr.Vector3([21., 0., -15.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 23
            [pyrr.Vector3([22., 0., -15.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 24
            [pyrr.Vector3([23., 0., -15.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 25
            [pyrr.Vector3([24., 0., -15.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 26
            [pyrr.Vector3([25., 0., -15.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 28
            [pyrr.Vector3([28., 0., -15.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 30
            [pyrr.Vector3([29., 0., -16.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],

            # 19

            # 1
            [pyrr.Vector3([1., 0., -16.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 3
            [pyrr.Vector3([2., 0., -17.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 4
            [pyrr.Vector3([4., 0., -16.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 9
            [pyrr.Vector3([8., 0., -17.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 11
            [pyrr.Vector3([11., 0., -17.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 13
            [pyrr.Vector3([13., 0., -16.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 15
            [pyrr.Vector3([14., 0., -17.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 16
            [pyrr.Vector3([16., 0., -16.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 19
            [pyrr.Vector3([19., 0., -17.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 20
            [pyrr.Vector3([20., 0., -17.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 23
            [pyrr.Vector3([23., 0., -17.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 24
            [pyrr.Vector3([24., 0., -17.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 25
            [pyrr.Vector3([25., 0., -17.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 26
            [pyrr.Vector3([26., 0., -17.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 27
            [pyrr.Vector3([27., 0., -17.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 30
            [pyrr.Vector3([29., 0., -17.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],

            # 20

            # 1
            [pyrr.Vector3([1., 0., -17.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 3
            [pyrr.Vector3([2., 0., -18.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 4
            [pyrr.Vector3([4., 0., -17.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 9
            [pyrr.Vector3([8., 0., -18.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 10
            [pyrr.Vector3([10., 0., -17.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 12
            [pyrr.Vector3([11., 0., -18.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 13
            [pyrr.Vector3([13., 0., -17.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 15
            [pyrr.Vector3([14., 0., -18.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 16
            [pyrr.Vector3([16., 0., -17.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 21
            [pyrr.Vector3([20., 0., -18.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 22
            [pyrr.Vector3([22., 0., -17.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 30
            [pyrr.Vector3([29., 0., -18.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],

            # 21

            # 1
            [pyrr.Vector3([1., 0., -18.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 3
            [pyrr.Vector3([2., 0., -19.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 4
            [pyrr.Vector3([4., 0., -18.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 7
            [pyrr.Vector3([6., 0., -18.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 8
            [pyrr.Vector3([7., 0., -18.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 10
            [pyrr.Vector3([10., 0., -18.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 12
            [pyrr.Vector3([11., 0., -19.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 13
            [pyrr.Vector3([13., 0., -18.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 15
            [pyrr.Vector3([14., 0., -19.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 17
            [pyrr.Vector3([16., 0., -18.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 18
            [pyrr.Vector3([17., 0., -18.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 21
            [pyrr.Vector3([20., 0., -19.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 22
            [pyrr.Vector3([22., 0., -18.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 25
            [pyrr.Vector3([24., 0., -18.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 26
            [pyrr.Vector3([25., 0., -18.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 27
            [pyrr.Vector3([26., 0., -18.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 28
            [pyrr.Vector3([27., 0., -18.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 29
            [pyrr.Vector3([28., 0., -18.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1., 1.5, 1.])],

            # 22

            # 1
            [pyrr.Vector3([1., 0., -19.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 3
            [pyrr.Vector3([2., 0., -20.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 4
            [pyrr.Vector3([4., 0., -19.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 6
            [pyrr.Vector3([5., 0., -20.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 8
            [pyrr.Vector3([8., 0., -20.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 9
            [pyrr.Vector3([9., 0., -20.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 12
            [pyrr.Vector3([11., 0., -20.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 13
            [pyrr.Vector3([13., 0., -19.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 16
            [pyrr.Vector3([16., 0., -20.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 17
            [pyrr.Vector3([17., 0., -20.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 19
            [pyrr.Vector3([19., 0., -19.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 25
            [pyrr.Vector3([25., 0., -20.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 26
            [pyrr.Vector3([26., 0., -20.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 27
            [pyrr.Vector3([27., 0., -20.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 28
            [pyrr.Vector3([28., 0., -20.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 29
            [pyrr.Vector3([29., 0., -20.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1., 1.5, 1.])],

            # 23

            # 1
            [pyrr.Vector3([1., 0., -20.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 3
            [pyrr.Vector3([2., 0., -21.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 4
            [pyrr.Vector3([4., 0., -20.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 6
            [pyrr.Vector3([5., 0., -21.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 7
            [pyrr.Vector3([7., 0., -20.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 12
            [pyrr.Vector3([11., 0., -21.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 13
            [pyrr.Vector3([13., 0., -20.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 18
            [pyrr.Vector3([17., 0., -21.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 19
            [pyrr.Vector3([19., 0., -20.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 30
            [pyrr.Vector3([29., 0., -21.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],

            # 24

            # 1
            [pyrr.Vector3([1., 0., -21.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 3
            [pyrr.Vector3([2., 0., -22.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 4
            [pyrr.Vector3([4., 0., -21.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 6
            [pyrr.Vector3([5., 0., -22.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 7
            [pyrr.Vector3([7., 0., -21.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 12
            [pyrr.Vector3([11., 0., -22.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 14
            [pyrr.Vector3([13., 0., -21.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 15
            [pyrr.Vector3([14., 0., -21.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 18
            [pyrr.Vector3([17., 0., -22.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 20
            [pyrr.Vector3([19., 0., -21.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 21
            [pyrr.Vector3([20., 0., -21.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 22
            [pyrr.Vector3([21., 0., -21.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 23
            [pyrr.Vector3([22., 0., -21.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 24
            [pyrr.Vector3([23., 0., -21.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 30
            [pyrr.Vector3([29., 0., -22.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],

            # 25

            # 1
            [pyrr.Vector3([1., 0., -22.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 3
            [pyrr.Vector3([2., 0., -23.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 4
            [pyrr.Vector3([4., 0., -22.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 9
            [pyrr.Vector3([8., 0., -23.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 10
            [pyrr.Vector3([10., 0., -22.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 13
            [pyrr.Vector3([13., 0., -23.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 14
            [pyrr.Vector3([14., 0., -23.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 16
            [pyrr.Vector3([16., 0., -22.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 18
            [pyrr.Vector3([17., 0., -23.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 20
            [pyrr.Vector3([20., 0., -23.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 23
            [pyrr.Vector3([23., 0., -23.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 24
            [pyrr.Vector3([24., 0., -23.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 27
            [pyrr.Vector3([26., 0., -23.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 28
            [pyrr.Vector3([28., 0., -22.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 30
            [pyrr.Vector3([29., 0., -23.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],

            # 26

            # 1
            [pyrr.Vector3([1., 0., -23.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 3
            [pyrr.Vector3([2., 0., -24.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 4
            [pyrr.Vector3([4., 0., -23.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 9
            [pyrr.Vector3([8., 0., -24.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 10
            [pyrr.Vector3([10., 0., -23.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 15
            [pyrr.Vector3([14., 0., -24.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 16
            [pyrr.Vector3([16., 0., -23.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 18
            [pyrr.Vector3([17., 0., -24.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 19
            [pyrr.Vector3([19., 0., -23.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 21
            [pyrr.Vector3([20., 0., -24.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 22
            [pyrr.Vector3([22., 0., -23.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 27
            [pyrr.Vector3([26., 0., -24.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 28
            [pyrr.Vector3([28., 0., -23.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 30
            [pyrr.Vector3([29., 0., -24.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],

            # 27

            # 1
            [pyrr.Vector3([1., 0., -24.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 3
            [pyrr.Vector3([2., 0., -25.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 5
            [pyrr.Vector3([4., 0., -24.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 6
            [pyrr.Vector3([5., 0., -24.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 9
            [pyrr.Vector3([8., 0., -25.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 10
            [pyrr.Vector3([10., 0., -24.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 13
            [pyrr.Vector3([12., 0., -24.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 14
            [pyrr.Vector3([13., 0., -24.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 16
            [pyrr.Vector3([16., 0., -24.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 18
            [pyrr.Vector3([17., 0., -25.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 19
            [pyrr.Vector3([19., 0., -24.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 21
            [pyrr.Vector3([20., 0., -25.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 22
            [pyrr.Vector3([22., 0., -24.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 27
            [pyrr.Vector3([26., 0., -25.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 29
            [pyrr.Vector3([28., 0., -24.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1., 1.5, 1.])],

            # 28

            # 1
            [pyrr.Vector3([1., 0., -25.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 4
            [pyrr.Vector3([4., 0., -26.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 5
            [pyrr.Vector3([5., 0., -26.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 6
            [pyrr.Vector3([6., 0., -26.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 9
            [pyrr.Vector3([8., 0., -26.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 10
            [pyrr.Vector3([10., 0., -25.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 12
            [pyrr.Vector3([11., 0., -26.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 14
            [pyrr.Vector3([14., 0., -26.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 15
            [pyrr.Vector3([15., 0., -26.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 18
            [pyrr.Vector3([17., 0., -26.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 19
            [pyrr.Vector3([19., 0., -25.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 24
            [pyrr.Vector3([23., 0., -26.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 25
            [pyrr.Vector3([25., 0., -25.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 28
            [pyrr.Vector3([28., 0., -26.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 29
            [pyrr.Vector3([29., 0., -26.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1., 1.5, 1.])],

            # 29

            # 1
            [pyrr.Vector3([1., 0., -26.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 9
            [pyrr.Vector3([8., 0., -27.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 10
            [pyrr.Vector3([10., 0., -26.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 12
            [pyrr.Vector3([11., 0., -27.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 13
            [pyrr.Vector3([13., 0., -26.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 18
            [pyrr.Vector3([17., 0., -27.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 19
            [pyrr.Vector3([19., 0., -26.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 24
            [pyrr.Vector3([23., 0., -27.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 25
            [pyrr.Vector3([25., 0., -26.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 30
            [pyrr.Vector3([29., 0., -27.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1., 1.5, 1.])],

            # 30

            # 2
            [pyrr.Vector3([1., 0., -27.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 3
            [pyrr.Vector3([2., 0., -27.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 4
            [pyrr.Vector3([3., 0., -27.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 5
            [pyrr.Vector3([4., 0., -27.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 6
            [pyrr.Vector3([5., 0., -27.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 7
            [pyrr.Vector3([6., 0., -27.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 8
            [pyrr.Vector3([7., 0., -27.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 11
            [pyrr.Vector3([10., 0., -27.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 13
            [pyrr.Vector3([13., 0., -27.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 16
            [pyrr.Vector3([15., 0., -27.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 17
            [pyrr.Vector3([16., 0., -27.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 20
            [pyrr.Vector3([19., 0., -27.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 21
            [pyrr.Vector3([20., 0., -27.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 22
            [pyrr.Vector3([21., 0., -27.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 23
            [pyrr.Vector3([22., 0., -27.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 26
            [pyrr.Vector3([25., 0., -27.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 27
            [pyrr.Vector3([26., 0., -27.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 28
            [pyrr.Vector3([27., 0., -27.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1., 1.5, 1.])],
            # 29
            [pyrr.Vector3([28., 0., -27.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1., 1.5, 1.])],

            # 31

            # 14
            [pyrr.Vector3([13., 0., -28.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1., 1.5, 1.])],
        ])
        for coords in self.wall_coords:
            new_actor = actor.Actor(
                    sp.Spawnpoint(*coords), self.wall_model
                )
            self.walls.append(new_actor)
            self.labirinth_collision.append(new_actor)
        model_identity = pyrr.Matrix44.identity()
        model_matrices = list()
        for wall in self.walls:
            model_inst = model_identity * wall.get_model_matrix()
            model_matrices.append(model_inst)
        model_matrices = numpy.array(model_matrices, dtype=numpy.float32)

        self.wall_model.prepare_instanced_draw(model_matrices)

    def load_wall_corner_out(self):
        self.wall_corner_out_model = model.Model("resources/wall/wall_corner_out.obj", "resources/wall/wall_corner_out.mtl")
        self.wall_corner_out_coords = numpy.array([
            # 1

            # 16
            [pyrr.Vector3([16., 0., 2.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1.051, 1.575, 1.051])],

            # 3

            # 3
            [pyrr.Vector3([2., 0., -1.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1.051, 1.575, 1.051])],
            # 7
            [pyrr.Vector3([6., 0., 0.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1.051, 1.575, 1.051])],
            # 9
            [pyrr.Vector3([8., 0., -1.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1.051, 1.575, 1.051])],
            # 10
            [pyrr.Vector3([9., 0., 0.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1.051, 1.575, 1.051])],
            # 12
            [pyrr.Vector3([11., 0., -1.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1.051, 1.575, 1.051])],
            # 16
            [pyrr.Vector3([15., 0., 0.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1.051, 1.575, 1.051])],
            # 21
            [pyrr.Vector3([20., 0., -1.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1.051, 1.575, 1.051])],
            # 22
            [pyrr.Vector3([21., 0., 0.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1.051, 1.575, 1.051])],
            # 24
            [pyrr.Vector3([23., 0., -1.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1.051, 1.575, 1.051])],
            # 28
            [pyrr.Vector3([27., 0., 0.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1.051, 1.575, 1.051])],

            # 4

            # 7
            [pyrr.Vector3([7., 0., -1.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1.051, 1.575, 1.051])],
            # 12
            [pyrr.Vector3([12., 0., -2.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1.051, 1.575, 1.051])],
            # 18
            [pyrr.Vector3([18., 0., -2.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1.051, 1.575, 1.051])],
            # 19
            [pyrr.Vector3([19., 0., -1.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1.051, 1.575, 1.051])],
            # 28
            [pyrr.Vector3([28., 0., -1.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1.051, 1.575, 1.051])],

            # 6

            # 7
            [pyrr.Vector3([6., 0., -3.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1.051, 1.575, 1.051])],
            # 27
            [pyrr.Vector3([26., 0., -4.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1.051, 1.575, 1.051])],

            # 7

            # 3
            [pyrr.Vector3([3., 0., -5.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1.051, 1.575, 1.051])],
            # 9
            [pyrr.Vector3([9., 0., -5.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1.051, 1.575, 1.051])],
            # 25
            [pyrr.Vector3([25., 0., -4.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1.051, 1.575, 1.051])],
            # 27
            [pyrr.Vector3([27., 0., -5.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1.051, 1.575, 1.051])],

            # 9

            # 3
            [pyrr.Vector3([2., 0., -7.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1.051, 1.575, 1.051])],
            # 4
            [pyrr.Vector3([3., 0., -6.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1.051, 1.575, 1.051])],
            # 15
            [pyrr.Vector3([14., 0., -7.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1.051, 1.575, 1.051])],
            # 28
            [pyrr.Vector3([27., 0., -6.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1.051, 1.575, 1.051])],

            # 10

            # 19
            [pyrr.Vector3([19., 0., -7.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1.051, 1.575, 1.051])],
            # 28
            [pyrr.Vector3([28., 0., -7.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1.051, 1.575, 1.051])],

            # 12

            # 10
            [pyrr.Vector3([9., 0., -9.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1.051, 1.575, 1.051])],
            # 18
            [pyrr.Vector3([17., 0., -10.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1.051, 1.575, 1.051])],
            # 25
            [pyrr.Vector3([24., 0., -9.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1.051, 1.575, 1.051])],
            # 27
            [pyrr.Vector3([26., 0., -10.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1.051, 1.575, 1.051])],
            # 28
            [pyrr.Vector3([27., 0., -9.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1.051, 1.575, 1.051])],

            # 13

            # 4
            [pyrr.Vector3([4., 0., -10.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1.051, 1.575, 1.051])],
            # 10
            [pyrr.Vector3([10., 0., -10.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1.051, 1.575, 1.051])],
            # 12
            [pyrr.Vector3([12., 0., -11.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1.051, 1.575, 1.051])],
            # 13
            [pyrr.Vector3([13., 0., -10.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1.051, 1.575, 1.051])],
            # 25
            [pyrr.Vector3([25., 0., -10.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1.051, 1.575, 1.051])],

            # 15

            # 3
            [pyrr.Vector3([2., 0., -13.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1.051, 1.575, 1.051])],
            # 9
            [pyrr.Vector3([8., 0., -13.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1.051, 1.575, 1.051])],
            # 21
            [pyrr.Vector3([20., 0., -13.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1.051, 1.575, 1.051])],

            # 16

            # 9
            [pyrr.Vector3([9., 0., -14.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1.051, 1.575, 1.051])],
            # 21
            [pyrr.Vector3([21., 0., -14.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1.051, 1.575, 1.051])],

            # 18

            # 9
            [pyrr.Vector3([8., 0., -16.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1.051, 1.575, 1.051])],
            # 13
            [pyrr.Vector3([12., 0., -15.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1.051, 1.575, 1.051])],

            # 19

            # 6
            [pyrr.Vector3([6., 0., -17.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1.051, 1.575, 1.051])],
            # 7
            [pyrr.Vector3([7., 0., -16.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1.051, 1.575, 1.051])],
            # 18
            [pyrr.Vector3([18., 0., -17.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1.051, 1.575, 1.051])],
            # 28
            [pyrr.Vector3([28., 0., -16.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1.051, 1.575, 1.051])],

            # 21

            # 6
            [pyrr.Vector3([5., 0., -19.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1.051, 1.575, 1.051])],
            # 19
            [pyrr.Vector3([18., 0., -18.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1.051, 1.575, 1.051])],
            # 24
            [pyrr.Vector3([23., 0., -19.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1.051, 1.575, 1.051])],

            # 22

            # 10
            [pyrr.Vector3([10., 0., -19.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1.051, 1.575, 1.051])],
            # 15
            [pyrr.Vector3([15., 0., -20.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1.051, 1.575, 1.051])],
            # 21
            [pyrr.Vector3([21., 0., -20.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1.051, 1.575, 1.051])],
            # 22
            [pyrr.Vector3([22., 0., -19.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1.051, 1.575, 1.051])],
            # 24
            [pyrr.Vector3([24., 0., -20.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1.051, 1.575, 1.051])],

            # 24

            # 9
            [pyrr.Vector3([8., 0., -22.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1.051, 1.575, 1.051])],
            # 10
            [pyrr.Vector3([9., 0., -21.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1.051, 1.575, 1.051])],
            # 16
            [pyrr.Vector3([15., 0., -21.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1.051, 1.575, 1.051])],
            # 25
            [pyrr.Vector3([24., 0., -21.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1.051, 1.575, 1.051])],
            # 27
            [pyrr.Vector3([26., 0., -22.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1.051, 1.575, 1.051])],
            # 28
            [pyrr.Vector3([27., 0., -21.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1.051, 1.575, 1.051])],

            # 25

            # 6
            [pyrr.Vector3([6., 0., -23.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1.051, 1.575, 1.051])],
            # 7
            [pyrr.Vector3([7., 0., -22.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1.051, 1.575, 1.051])],
            # 12
            [pyrr.Vector3([12., 0., -23.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1.051, 1.575, 1.051])],
            # 25
            [pyrr.Vector3([25., 0., -22.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1.051, 1.575, 1.051])],

            # 27

            # 7
            [pyrr.Vector3([6., 0., -24.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1.051, 1.575, 1.051])],
            # 12
            [pyrr.Vector3([11., 0., -25.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1.051, 1.575, 1.051])],
            # 24
            [pyrr.Vector3([23., 0., -25.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1.051, 1.575, 1.051])],
            # 25
            [pyrr.Vector3([24., 0., -24.]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([1.051, 1.575, 1.051])],

            # 28

            # 3
            [pyrr.Vector3([3., 0., -26.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1.051, 1.575, 1.051])],
            # 7
            [pyrr.Vector3([7., 0., -25.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1.051, 1.575, 1.051])],
            # 16
            [pyrr.Vector3([16., 0., -25.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1.051, 1.575, 1.051])],
            # 21
            [pyrr.Vector3([21., 0., -26.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1.051, 1.575, 1.051])],
            # 22
            [pyrr.Vector3([22., 0., -25.]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([1.051, 1.575, 1.051])],
            # 27
            [pyrr.Vector3([27., 0., -26.]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([1.051, 1.575, 1.051])],

            # 30

            # 15
            [pyrr.Vector3([14., 0., -28.]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([1.051, 1.575, 1.051])],
        ])
        for coords in self.wall_corner_out_coords:
            new_actor = actor.Actor(
                    sp.Spawnpoint(*coords), self.wall_corner_out_model
                )
            self.wall_corner_out.append(new_actor)
            self.labirinth_collision.append(new_actor)
        model_identity = pyrr.Matrix44.identity()
        model_matrices = list()
        for wall_corner in self.wall_corner_out:
            model_inst = model_identity * wall_corner.get_model_matrix()
            model_matrices.append(model_inst)
        model_matrices = numpy.array(model_matrices, dtype=numpy.float32)

        self.wall_corner_out_model.prepare_instanced_draw(model_matrices)

    def load_floors(self):
        self.floor_model = model.Model("resources/floor/floor.obj", "resources/floor/floor.mtl")
        self.floor_coords = numpy.array([
            # 2

            # 3-4
            [pyrr.Vector3([3., 0.2, 0.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([1.2, 1., 0.75])],
            # 5-6
            [pyrr.Vector3([5., 0.2, 0.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([1.2, 1., 0.75])],
            # 6-7
            [pyrr.Vector3([6., 0.2, 0.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([1.2, 1., 0.75])],
            # 9-10
            [pyrr.Vector3([9., 0.2, 0.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([1.2, 1., 0.75])],
            # 12-13
            [pyrr.Vector3([12., 0.2, 0.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([1.2, 1., 0.75])],
            # 14-15
            [pyrr.Vector3([14., 0.2, 0.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([1.2, 1., 0.75])],
            # 15-16
            [pyrr.Vector3([15., 0.2, 0.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([1.2, 1., 0.75])],
            # 21-22
            [pyrr.Vector3([21., 0.2, 0.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([1.2, 1., 0.75])],
            # 24-25
            [pyrr.Vector3([24., 0.2, 0.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([1.2, 1., 0.75])],
            # 26-27
            [pyrr.Vector3([26., 0.2, 0.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([1.2, 1., 0.75])],
            # 27-28
            [pyrr.Vector3([27., 0.2, 0.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([1.2, 1., 0.75])],

            # 3

            # 2
            [pyrr.Vector3([1.5, 0.2, -1.]), pyrr.Vector3([0., 90, 0.]), pyrr.Vector3([1.2, 1., 0.75])],
            # 8
            [pyrr.Vector3([7.5, 0.2, -1.]), pyrr.Vector3([0., 90, 0.]), pyrr.Vector3([1.2, 1., 0.75])],
            # 11
            [pyrr.Vector3([10.5, 0.2, -1.]), pyrr.Vector3([0., 90, 0.]), pyrr.Vector3([1.2, 1., 0.75])],
            # 17
            [pyrr.Vector3([16.5, 0.2, -1.]), pyrr.Vector3([0., 90, 0.]), pyrr.Vector3([1.2, 1., 0.75])],
            # 20
            [pyrr.Vector3([19.5, 0.2, -1.]), pyrr.Vector3([0., 90, 0.]), pyrr.Vector3([1.2, 1., 0.75])],
            # 23
            [pyrr.Vector3([22.5, 0.2, -1.]), pyrr.Vector3([0., 90, 0.]), pyrr.Vector3([1.2, 1., 0.75])],
            # 29
            [pyrr.Vector3([28.5, 0.2, -1.]), pyrr.Vector3([0., 90, 0.]), pyrr.Vector3([1.2, 1., 0.75])],

            # 4

            # 23
            [pyrr.Vector3([22.5, 0.2, -2.]), pyrr.Vector3([0., 90, 0.]), pyrr.Vector3([1.2, 1., 0.75])],

            # 5

            # 2
            [pyrr.Vector3([1.5, 0.2, -3.]), pyrr.Vector3([0., 90, 0.]), pyrr.Vector3([1.2, 1., 0.75])],
            # 5-6
            [pyrr.Vector3([5., 0.2, -2.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([1.2, 1., 0.75])],
            # 6-7
            [pyrr.Vector3([6., 0.2, -2.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([1.2, 1., 0.75])],
            # 12-13
            [pyrr.Vector3([12., 0.2, -2.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([1.2, 1., 0.75])],
            # 13-14
            [pyrr.Vector3([13., 0.2, -2.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([1.2, 1., 0.75])],
            # 18-19
            [pyrr.Vector3([18., 0.2, -2.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([1.2, 1., 0.75])],
            # 27-28
            [pyrr.Vector3([27., 0.2, -2.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([1.2, 1., 0.75])],

            # 6

            # 2
            [pyrr.Vector3([1.5, 0.2, -4.]), pyrr.Vector3([0., 90, 0.]), pyrr.Vector3([1.2, 1., 0.75])],
            # 8
            [pyrr.Vector3([7.5, 0.2, -4.]), pyrr.Vector3([0., 90, 0.]), pyrr.Vector3([1.2, 1., 0.75])],
            # 26
            [pyrr.Vector3([25.5, 0.2, -4.]), pyrr.Vector3([0., 90, 0.]), pyrr.Vector3([1.2, 1., 0.75])],

            # 8

            # 3-4
            [pyrr.Vector3([3., 0.2, -5.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([1.2, 1., 0.75])],
            # 9-10
            [pyrr.Vector3([9., 0.2, -5.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([1.2, 1., 0.75])],
            # 10-11
            [pyrr.Vector3([10., 0.2, -5.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([1.2, 1., 0.75])],
            # 15-16
            [pyrr.Vector3([15., 0.2, -5.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([1.2, 1., 0.75])],
            # 16-17
            [pyrr.Vector3([16., 0.2, -5.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([1.2, 1., 0.75])],
            # 23-24
            [pyrr.Vector3([23., 0.2, -5.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([1.2, 1., 0.75])],
            # 24-25
            [pyrr.Vector3([24., 0.2, -5.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([1.2, 1., 0.75])],
            # 27-28
            [pyrr.Vector3([27., 0.2, -5.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([1.2, 1., 0.75])],
            # 20
            [pyrr.Vector3([19.5, 0.2, -6.]), pyrr.Vector3([0., 90, 0.]), pyrr.Vector3([1.2, 1., 0.75])],

            # 9

            # 2
            [pyrr.Vector3([1.5, 0.2, -7.]), pyrr.Vector3([0., 90, 0.]), pyrr.Vector3([1.2, 1., 0.75])],
            # 5
            [pyrr.Vector3([4.5, 0.2, -7.]), pyrr.Vector3([0., 90, 0.]), pyrr.Vector3([1.2, 1., 0.75])],
            # 14
            [pyrr.Vector3([13.5, 0.2, -7.]), pyrr.Vector3([0., 90, 0.]), pyrr.Vector3([1.2, 1., 0.75])],
            # 20
            [pyrr.Vector3([19.5, 0.2, -7.]), pyrr.Vector3([0., 90, 0.]), pyrr.Vector3([1.2, 1., 0.75])],
            # 29
            [pyrr.Vector3([28.5, 0.2, -7.]), pyrr.Vector3([0., 90, 0.]), pyrr.Vector3([1.2, 1., 0.75])],

            # 10

            # 2
            [pyrr.Vector3([1.5, 0.2, -8.]), pyrr.Vector3([0., 90, 0.]), pyrr.Vector3([1.2, 1., 0.75])],

            # 11

            # 5
            [pyrr.Vector3([4.5, 0.2, -9.]), pyrr.Vector3([0., 90, 0.]), pyrr.Vector3([1.2, 1., 0.75])],
            # 8-9
            [pyrr.Vector3([8., 0.2, -8.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([1.2, 1., 0.75])],
            # 9-10
            [pyrr.Vector3([9., 0.2, -8.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([1.2, 1., 0.75])],
            # 14
            [pyrr.Vector3([13.5, 0.2, -9.]), pyrr.Vector3([0., 90, 0.]), pyrr.Vector3([1.2, 1., 0.75])],
            # 18-19
            [pyrr.Vector3([18., 0.2, -8.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([1.2, 1., 0.75])],
            # 23-24
            [pyrr.Vector3([23., 0.2, -8.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([1.2, 1., 0.75])],
            # 24-25
            [pyrr.Vector3([24., 0.2, -8.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([1.2, 1., 0.75])],
            # 27-28
            [pyrr.Vector3([27., 0.2, -8.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([1.2, 1., 0.75])],

            # 12

            # 5
            [pyrr.Vector3([4.5, 0.2, -10.]), pyrr.Vector3([0., 90, 0.]), pyrr.Vector3([1.2, 1., 0.75])],
            # 11
            [pyrr.Vector3([10.5, 0.2, -10.]), pyrr.Vector3([0., 90, 0.]), pyrr.Vector3([1.2, 1., 0.75])],
            # 14
            [pyrr.Vector3([13.5, 0.2, -10.]), pyrr.Vector3([0., 90, 0.]), pyrr.Vector3([1.2, 1., 0.75])],
            # 17
            [pyrr.Vector3([16.5, 0.2, -10.]), pyrr.Vector3([0., 90, 0.]), pyrr.Vector3([1.2, 1., 0.75])],
            # 26
            [pyrr.Vector3([25.5, 0.2, -10.]), pyrr.Vector3([0., 90, 0.]), pyrr.Vector3([1.2, 1., 0.75])],
            # 29
            [pyrr.Vector3([28.5, 0.2, -10.]), pyrr.Vector3([0., 90, 0.]), pyrr.Vector3([1.2, 1., 0.75])],

            # 14

            # 3-4
            [pyrr.Vector3([3., 0.2, -11.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([1.2, 1., 0.75])],
            # 9-10
            [pyrr.Vector3([9., 0.2, -11.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([1.2, 1., 0.75])],
            # 12-13
            [pyrr.Vector3([12., 0.2, -11.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([1.2, 1., 0.75])],
            # 17
            [pyrr.Vector3([16.5, 0.2, -12.]), pyrr.Vector3([0., 90, 0.]), pyrr.Vector3([1.2, 1., 0.75])],
            # 21-22
            [pyrr.Vector3([21., 0.2, -11.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([1.2, 1., 0.75])],
            # 23-24
            [pyrr.Vector3([23., 0.2, -11.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([1.2, 1., 0.75])],
            # 24-25
            [pyrr.Vector3([24., 0.2, -11.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([1.2, 1., 0.75])],
            # 29
            [pyrr.Vector3([28.5, 0.2, -12.]), pyrr.Vector3([0., 90, 0.]), pyrr.Vector3([1.2, 1., 0.75])],

            # 15

            # 2
            [pyrr.Vector3([1.5, 0.2, -13.]), pyrr.Vector3([0., 90, 0.]), pyrr.Vector3([1.2, 1., 0.75])],
            # 8
            [pyrr.Vector3([7.5, 0.2, -13.]), pyrr.Vector3([0., 90, 0.]), pyrr.Vector3([1.2, 1., 0.75])],
            # 20
            [pyrr.Vector3([19.5, 0.2, -13.]), pyrr.Vector3([0., 90, 0.]), pyrr.Vector3([1.2, 1., 0.75])],

            # 16

            # 17
            [pyrr.Vector3([16.5, 0.2, -14.]), pyrr.Vector3([0., 90, 0.]), pyrr.Vector3([1.2, 1., 0.75])],
            # 29
            [pyrr.Vector3([28.5, 0.2, -14.]), pyrr.Vector3([0., 90, 0.]), pyrr.Vector3([1.2, 1., 0.75])],

            # 17

            # 2
            [pyrr.Vector3([1.5, 0.2, -15.]), pyrr.Vector3([0., 90, 0.]), pyrr.Vector3([1.2, 1., 0.75])],
            # 5
            [pyrr.Vector3([4.5, 0.2, -15.]), pyrr.Vector3([0., 90, 0.]), pyrr.Vector3([1.2, 1., 0.75])],
            # 9-10
            [pyrr.Vector3([9., 0.2, -14.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([1.2, 1., 0.75])],
            # 11-12
            [pyrr.Vector3([11., 0.2, -14.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([1.2, 1., 0.75])],
            # 12-13
            [pyrr.Vector3([12., 0.2, -14.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([1.2, 1., 0.75])],
            # 21-22
            [pyrr.Vector3([21., 0.2, -14.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([1.2, 1., 0.75])],
            # 23-24
            [pyrr.Vector3([23., 0.2, -14.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([1.2, 1., 0.75])],
            # 25-26
            [pyrr.Vector3([25., 0.2, -14.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([1.2, 1., 0.75])],

            # 18

            # 5
            [pyrr.Vector3([4.5, 0.2, -16.]), pyrr.Vector3([0., 90, 0.]), pyrr.Vector3([1.2, 1., 0.75])],
            # 8
            [pyrr.Vector3([7.5, 0.2, -16.]), pyrr.Vector3([0., 90, 0.]), pyrr.Vector3([1.2, 1., 0.75])],
            # 14
            [pyrr.Vector3([13.5, 0.2, -16.]), pyrr.Vector3([0., 90, 0.]), pyrr.Vector3([1.2, 1., 0.75])],
            # 17
            [pyrr.Vector3([16.5, 0.2, -16.]), pyrr.Vector3([0., 90, 0.]), pyrr.Vector3([1.2, 1., 0.75])],
            # 29
            [pyrr.Vector3([28.5, 0.2, -16.]), pyrr.Vector3([0., 90, 0.]), pyrr.Vector3([1.2, 1., 0.75])],

            # 19

            # 2
            [pyrr.Vector3([1.5, 0.2, -17.]), pyrr.Vector3([0., 90, 0.]), pyrr.Vector3([1.2, 1., 0.75])],

            # 20

            # 6-7
            [pyrr.Vector3([6., 0.2, -17.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([1.2, 1., 0.75])],
            # 11
            [pyrr.Vector3([10.5, 0.2, -18.]), pyrr.Vector3([0., 90, 0.]), pyrr.Vector3([1.2, 1., 0.75])],
            # 14
            [pyrr.Vector3([13.5, 0.2, -18.]), pyrr.Vector3([0., 90, 0.]), pyrr.Vector3([1.2, 1., 0.75])],
            # 18-19
            [pyrr.Vector3([18., 0.2, -17.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([1.2, 1., 0.75])],
            # 24-25
            [pyrr.Vector3([24., 0.2, -17.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([1.2, 1., 0.75])],
            # 26-27
            [pyrr.Vector3([26., 0.2, -17.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([1.2, 1., 0.75])],
            # 27-28
            [pyrr.Vector3([27., 0.2, -17.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([1.2, 1., 0.75])],

            # 21

            # 2
            [pyrr.Vector3([1.5, 0.2, -19.]), pyrr.Vector3([0., 90, 0.]), pyrr.Vector3([1.2, 1., 0.75])],
            # 5
            [pyrr.Vector3([4.5, 0.2, -19.]), pyrr.Vector3([0., 90, 0.]), pyrr.Vector3([1.2, 1., 0.75])],
            # 11
            [pyrr.Vector3([10.5, 0.2, -19.]), pyrr.Vector3([0., 90, 0.]), pyrr.Vector3([1.2, 1., 0.75])],
            # 14
            [pyrr.Vector3([13.5, 0.2, -19.]), pyrr.Vector3([0., 90, 0.]), pyrr.Vector3([1.2, 1., 0.75])],
            # 20
            [pyrr.Vector3([19.5, 0.2, -19.]), pyrr.Vector3([0., 90, 0.]), pyrr.Vector3([1.2, 1., 0.75])],
            # 23
            [pyrr.Vector3([22.5, 0.2, -19.]), pyrr.Vector3([0., 90, 0.]), pyrr.Vector3([1.2, 1., 0.75])],

            # 23

            # 2
            [pyrr.Vector3([1.5, 0.2, -21.]), pyrr.Vector3([0., 90, 0.]), pyrr.Vector3([1.2, 1., 0.75])],
            # 5
            [pyrr.Vector3([4.5, 0.2, -21.]), pyrr.Vector3([0., 90, 0.]), pyrr.Vector3([1.2, 1., 0.75])],
            # 9-10
            [pyrr.Vector3([9., 0.2, -20.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([1.2, 1., 0.75])],
            # 15-16
            [pyrr.Vector3([15., 0.2, -20.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([1.2, 1., 0.75])],
            # 21-22
            [pyrr.Vector3([21., 0.2, -20.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([1.2, 1., 0.75])],
            # 24-25
            [pyrr.Vector3([24., 0.2, -20.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([1.2, 1., 0.75])],
            # 27-28
            [pyrr.Vector3([27., 0.2, -20.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([1.2, 1., 0.75])],

            # 24

            # 5
            [pyrr.Vector3([4.5, 0.2, -22.]), pyrr.Vector3([0., 90, 0.]), pyrr.Vector3([1.2, 1., 0.75])],
            # 8
            [pyrr.Vector3([7.5, 0.2, -22.]), pyrr.Vector3([0., 90, 0.]), pyrr.Vector3([1.2, 1., 0.75])],
            # 11
            [pyrr.Vector3([10.5, 0.2, -22.]), pyrr.Vector3([0., 90, 0.]), pyrr.Vector3([1.2, 1., 0.75])],
            # 17
            [pyrr.Vector3([16.5, 0.2, -22.]), pyrr.Vector3([0., 90, 0.]), pyrr.Vector3([1.2, 1., 0.75])],
            # 26
            [pyrr.Vector3([25.5, 0.2, -22.]), pyrr.Vector3([0., 90, 0.]), pyrr.Vector3([1.2, 1., 0.75])],
            # 29
            [pyrr.Vector3([28.5, 0.2, -22.]), pyrr.Vector3([0., 90, 0.]), pyrr.Vector3([1.2, 1., 0.75])],

            # 25

            # 2
            [pyrr.Vector3([1.5, 0.2, -23.]), pyrr.Vector3([0., 90, 0.]), pyrr.Vector3([1.2, 1., 0.75])],
            # 26
            [pyrr.Vector3([25.5, 0.2, -23.]), pyrr.Vector3([0., 90, 0.]), pyrr.Vector3([1.2, 1., 0.75])],
            # 29
            [pyrr.Vector3([28.5, 0.2, -23.]), pyrr.Vector3([0., 90, 0.]), pyrr.Vector3([1.2, 1., 0.75])],

            # 26

            # 6-7
            [pyrr.Vector3([6., 0.2, -23.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([1.2, 1., 0.75])],
            # 12-13
            [pyrr.Vector3([12., 0.2, -23.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([1.2, 1., 0.75])],
            # 13-14
            [pyrr.Vector3([13., 0.2, -23.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([1.2, 1., 0.75])],
            # 17
            [pyrr.Vector3([16.5, 0.2, -24.]), pyrr.Vector3([0., 90, 0.]), pyrr.Vector3([1.2, 1., 0.75])],
            # 20
            [pyrr.Vector3([19.5, 0.2, -24.]), pyrr.Vector3([0., 90, 0.]), pyrr.Vector3([1.2, 1., 0.75])],
            # 24-25
            [pyrr.Vector3([24., 0.2, -23.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([1.2, 1., 0.75])],

            # 27

            # 2
            [pyrr.Vector3([1.5, 0.2, -25.]), pyrr.Vector3([0., 90, 0.]), pyrr.Vector3([1.2, 1., 0.75])],
            # 8
            [pyrr.Vector3([7.5, 0.2, -25.]), pyrr.Vector3([0., 90, 0.]), pyrr.Vector3([1.2, 1., 0.75])],
            # 11
            [pyrr.Vector3([10.5, 0.2, -25.]), pyrr.Vector3([0., 90, 0.]), pyrr.Vector3([1.2, 1., 0.75])],
            # 17
            [pyrr.Vector3([16.5, 0.2, -25.]), pyrr.Vector3([0., 90, 0.]), pyrr.Vector3([1.2, 1., 0.75])],
            # 20
            [pyrr.Vector3([19.5, 0.2, -25.]), pyrr.Vector3([0., 90, 0.]), pyrr.Vector3([1.2, 1., 0.75])],
            # 23
            [pyrr.Vector3([22.5, 0.2, -25.]), pyrr.Vector3([0., 90, 0.]), pyrr.Vector3([1.2, 1., 0.75])],
            # 26
            [pyrr.Vector3([25.5, 0.2, -25.]), pyrr.Vector3([0., 90, 0.]), pyrr.Vector3([1.2, 1., 0.75])],

            # 28

            # 11
            [pyrr.Vector3([10.5, 0.2, -26.]), pyrr.Vector3([0., 90, 0.]), pyrr.Vector3([1.2, 1., 0.75])],

            # 29

            # 3-4
            [pyrr.Vector3([3., 0.2, -26.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([1.2, 1., 0.75])],
            # 5-6
            [pyrr.Vector3([5., 0.2, -26.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([1.2, 1., 0.75])],
            # 6-7
            [pyrr.Vector3([6., 0.2, -26.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([1.2, 1., 0.75])],
            # 15-16
            [pyrr.Vector3([15., 0.2, -26.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([1.2, 1., 0.75])],
            # 21-22
            [pyrr.Vector3([21., 0.2, -26.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([1.2, 1., 0.75])],
            # 27-28
            [pyrr.Vector3([27., 0.2, -26.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([1.2, 1., 0.75])],
            # 28-29
            [pyrr.Vector3([28., 0.2, -26.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([1.2, 1., 0.75])],
        ])
        for coords in self.floor_coords:
            new_actor = actor.Actor(
                    sp.Spawnpoint(*coords), self.floor_model
                )
            self.floors.append(new_actor)
        model_identity = pyrr.Matrix44.identity()
        model_matrices = list()
        for floor in self.floors:
            model_inst = model_identity * floor.get_model_matrix()
            model_matrices.append(model_inst)
        model_matrices = numpy.array(model_matrices, dtype=numpy.float32)

        self.floor_model.prepare_instanced_draw(model_matrices)

    def load_floor_rectangles(self):
        self.floor_rectangle_model = model.Model("resources/floor/floor_rectangle.obj", "resources/floor/floor_rectangle.mtl")
        self.floor_rectangle_coords = numpy.array([
            # 1

            # 17
            [pyrr.Vector3([16.5, 0.2, 1.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([0.5, 1., 0.5])],

            # 2

            # 2
            [pyrr.Vector3([1.5, 0.2, 0.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([0.5, 1., 0.5])],
            # 8
            [pyrr.Vector3([7.5, 0.2, 0.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([0.5, 1., 0.5])],
            # 11
            [pyrr.Vector3([10.5, 0.2, 0.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([0.5, 1., 0.5])],
            # 17
            [pyrr.Vector3([16.5, 0.2, 0.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([0.5, 1., 0.5])],
            # 20
            [pyrr.Vector3([19.5, 0.2, 0.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([0.5, 1., 0.5])],
            # 23
            [pyrr.Vector3([22.5, 0.2, 0.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([0.5, 1., 0.5])],
            # 29
            [pyrr.Vector3([28.5, 0.2, 0.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([0.5, 1., 0.5])],

            # 5

            # 8
            [pyrr.Vector3([7.5, 0.2, -2.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([0.5, 1., 0.5])],
            # 11
            [pyrr.Vector3([10.5, 0.2, -2.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([0.5, 1., 0.5])],
            # 17
            [pyrr.Vector3([16.5, 0.2, -2.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([0.5, 1., 0.5])],
            # 20
            [pyrr.Vector3([19.5, 0.2, -2.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([0.5, 1., 0.5])],
            # 26
            [pyrr.Vector3([25.5, 0.2, -2.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([0.5, 1., 0.5])],
            # 29
            [pyrr.Vector3([28.5, 0.2, -2.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([0.5, 1., 0.5])],

            # 8

            # 2
            [pyrr.Vector3([1.5, 0.2, -5.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([0.5, 1., 0.5])],
            # 5
            [pyrr.Vector3([4.5, 0.2, -5.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([0.5, 1., 0.5])],
            # 8
            [pyrr.Vector3([7.5, 0.2, -5.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([0.5, 1., 0.5])],
            # 14
            [pyrr.Vector3([13.5, 0.2, -5.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([0.5, 1., 0.5])],
            # 26
            [pyrr.Vector3([25.5, 0.2, -5.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([0.5, 1., 0.5])],
            # 29
            [pyrr.Vector3([28.5, 0.2, -5.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([0.5, 1., 0.5])],

            # 11

            # 11
            [pyrr.Vector3([10.5, 0.2, -8.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([0.5, 1., 0.5])],
            # 17
            [pyrr.Vector3([16.5, 0.2, -8.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([0.5, 1., 0.5])],
            # 20
            [pyrr.Vector3([19.5, 0.2, -8.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([0.5, 1., 0.5])],
            # 26
            [pyrr.Vector3([25.5, 0.2, -8.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([0.5, 1., 0.5])],
            # 29
            [pyrr.Vector3([28.5, 0.2, -8.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([0.5, 1., 0.5])],

            # 14

            # 2
            [pyrr.Vector3([1.5, 0.2, -11.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([0.5, 1., 0.5])],
            # 5
            [pyrr.Vector3([4.5, 0.2, -11.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([0.5, 1., 0.5])],
            # 8
            [pyrr.Vector3([7.5, 0.2, -11.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([0.5, 1., 0.5])],
            # 11
            [pyrr.Vector3([10.5, 0.2, -11.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([0.5, 1., 0.5])],
            # 14
            [pyrr.Vector3([13.5, 0.2, -11.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([0.5, 1., 0.5])],
            # 20
            [pyrr.Vector3([19.5, 0.2, -11.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([0.5, 1., 0.5])],
            # 26
            [pyrr.Vector3([25.5, 0.2, -11.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([0.5, 1., 0.5])],

            # 17

            # 8
            [pyrr.Vector3([7.5, 0.2, -14.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([0.5, 1., 0.5])],
            # 14
            [pyrr.Vector3([13.5, 0.2, -14.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([0.5, 1., 0.5])],
            # 20
            [pyrr.Vector3([19.5, 0.2, -14.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([0.5, 1., 0.5])],

            # 20

            # 5
            [pyrr.Vector3([4.5, 0.2, -17.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([0.5, 1., 0.5])],
            # 8
            [pyrr.Vector3([7.5, 0.2, -17.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([0.5, 1., 0.5])],
            # 17
            [pyrr.Vector3([16.5, 0.2, -17.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([0.5, 1., 0.5])],
            # 20
            [pyrr.Vector3([19.5, 0.2, -17.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([0.5, 1., 0.5])],
            # 23
            [pyrr.Vector3([22.5, 0.2, -17.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([0.5, 1., 0.5])],
            # 29
            [pyrr.Vector3([28.5, 0.2, -17.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([0.5, 1., 0.5])],

            # 23

            # 8
            [pyrr.Vector3([7.5, 0.2, -20.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([0.5, 1., 0.5])],
            # 11
            [pyrr.Vector3([10.5, 0.2, -20.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([0.5, 1., 0.5])],
            # 14
            [pyrr.Vector3([13.5, 0.2, -20.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([0.5, 1., 0.5])],
            # 17
            [pyrr.Vector3([16.5, 0.2, -20.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([0.5, 1., 0.5])],
            # 20
            [pyrr.Vector3([19.5, 0.2, -20.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([0.5, 1., 0.5])],
            # 23
            [pyrr.Vector3([22.5, 0.2, -20.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([0.5, 1., 0.5])],
            # 26
            [pyrr.Vector3([25.5, 0.2, -20.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([0.5, 1., 0.5])],
            # 29
            [pyrr.Vector3([28.5, 0.2, -20.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([0.5, 1., 0.5])],

            # 26

            # 5
            [pyrr.Vector3([4.5, 0.2, -23.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([0.5, 1., 0.5])],
            # 8
            [pyrr.Vector3([7.5, 0.2, -23.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([0.5, 1., 0.5])],
            # 11
            [pyrr.Vector3([10.5, 0.2, -23.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([0.5, 1., 0.5])],
            # 23
            [pyrr.Vector3([22.5, 0.2, -23.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([0.5, 1., 0.5])],
            # 26
            [pyrr.Vector3([25.5, 0.2, -23.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([0.5, 1., 0.5])],

            # 29

            # 2
            [pyrr.Vector3([1.5, 0.2, -26.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([0.5, 1., 0.5])],
            # 8
            [pyrr.Vector3([7.5, 0.2, -26.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([0.5, 1., 0.5])],
            # 14
            [pyrr.Vector3([13.5, 0.2, -26.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([0.5, 1., 0.5])],
            # 17
            [pyrr.Vector3([16.5, 0.2, -26.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([0.5, 1., 0.5])],
            # 20
            [pyrr.Vector3([19.5, 0.2, -26.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([0.5, 1., 0.5])],
            # 23
            [pyrr.Vector3([22.5, 0.2, -26.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([0.5, 1., 0.5])],
            # 26
            [pyrr.Vector3([25.5, 0.2, -26.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([0.5, 1., 0.5])],

            # 30

            # 14
            [pyrr.Vector3([13.5, 0.2, -27.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([0.5, 1., 0.5])],
        ])
        for coords in self.floor_rectangle_coords:
            new_actor = actor.Actor(
                    sp.Spawnpoint(*coords), self.floor_rectangle_model
                )
            self.floor_rectangles.append(new_actor)
        model_identity = pyrr.Matrix44.identity()
        model_matrices = list()
        for floor_rectangle in self.floor_rectangles:
            model_inst = model_identity * floor_rectangle.get_model_matrix()
            model_matrices.append(model_inst)
        model_matrices = numpy.array(model_matrices, dtype=numpy.float32)

        self.floor_rectangle_model.prepare_instanced_draw(model_matrices)

    def load_torches(self):
        self.torch_model = model.Model("resources/torch/torch.obj", "resources/torch/torch.mtl")
        self.torch_coords = numpy.array([
            # 2

            # 2
            [pyrr.Vector3([1.12, 1.2, 0.5]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([0.2, 0.2, 0.2])],
            # 11
            [pyrr.Vector3([10.5, 1.2, 0.88]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([0.2, 0.2, 0.2])],
            # 17
            [pyrr.Vector3([16.88, 1.2, 0.5]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([0.2, 0.2, 0.2])],
            # 23
            [pyrr.Vector3([22.5, 1.2, 0.88]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([0.2, 0.2, 0.2])],

            # 5

            # 8
            [pyrr.Vector3([7.88, 1.2, -2.5]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([0.2, 0.2, 0.2])],
            # 13
            [pyrr.Vector3([12.5, 1.2, -2.88]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([0.2, 0.2, 0.2])],
            # 20
            [pyrr.Vector3([19.5, 1.2, -2.88]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([0.2, 0.2, 0.2])],
            # 29
            [pyrr.Vector3([28.88, 1.2, -2.5]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([0.2, 0.2, 0.2])],

            # 8

            # 2
            [pyrr.Vector3([1.12, 1.2, -5.5]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([0.2, 0.2, 0.2])],
            # 10
            [pyrr.Vector3([9.5, 1.2, -5.12]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([0.2, 0.2, 0.2])],
            # 14
            [pyrr.Vector3([13.12, 1.2, -5.5]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([0.2, 0.2, 0.2])],
            # 26
            [pyrr.Vector3([25.5, 1.2, -5.88]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([0.2, 0.2, 0.2])],

            # 11

            # 5
            [pyrr.Vector3([4.88, 1.2, -8.5]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([0.2, 0.2, 0.2])],
            # 8
            [pyrr.Vector3([7.5, 1.2, -8.12]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([0.2, 0.2, 0.2])],
            # 20
            [pyrr.Vector3([19.88, 1.2, -8.5]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([0.2, 0.2, 0.2])],
            # 23
            [pyrr.Vector3([22.12, 1.2, -8.5]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([0.2, 0.2, 0.2])],
            # 29
            [pyrr.Vector3([28.88, 1.2, -8.5]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([0.2, 0.2, 0.2])],

            # 14

            # 2
            [pyrr.Vector3([1.5, 1.2, -11.12]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([0.2, 0.2, 0.2])],
            # 11
            [pyrr.Vector3([10.5, 1.2, -11.88]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([0.2, 0.2, 0.2])],
            # 20
            [pyrr.Vector3([19.5, 1.2, -11.12]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([0.2, 0.2, 0.2])],
            # 26
            [pyrr.Vector3([25.5, 1.2, -11.88]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([0.2, 0.2, 0.2])],

            # 15

            # 17
            [pyrr.Vector3([16.12, 1.2, -12.5]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([0.2, 0.2, 0.2])],

            # 17

            # 8
            [pyrr.Vector3([7.12, 1.2, -14.5]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([0.2, 0.2, 0.2])],
            # 26
            [pyrr.Vector3([25.88, 1.2, -14.5]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([0.2, 0.2, 0.2])],

            # 20

            # 5
            [pyrr.Vector3([4.12, 1.2, -17.5]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([0.2, 0.2, 0.2])],
            # 14
            [pyrr.Vector3([13.12, 1.2, -17.5]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([0.2, 0.2, 0.2])],
            # 20
            [pyrr.Vector3([19.5, 1.2, -17.12]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([0.2, 0.2, 0.2])],
            # 29
            [pyrr.Vector3([28.5, 1.2, -17.88]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([0.2, 0.2, 0.2])],

            # 21

            # 2
            [pyrr.Vector3([1.12, 1.2, -18.5]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([0.2, 0.2, 0.2])],

            # 23

            # 11
            [pyrr.Vector3([10.88, 1.2, -20.5]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([0.2, 0.2, 0.2])],
            # 17
            [pyrr.Vector3([16.88, 1.2, -20.5]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([0.2, 0.2, 0.2])],
            # 23
            [pyrr.Vector3([22.5, 1.2, -20.88]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([0.2, 0.2, 0.2])],
            # 29
            [pyrr.Vector3([28.5, 1.2, -20.12]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([0.2, 0.2, 0.2])],

            # 26

            # 8
            [pyrr.Vector3([7.88, 1.2, -23.5]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([0.2, 0.2, 0.2])],
            # 13
            [pyrr.Vector3([12.5, 1.2, -23.88]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([0.2, 0.2, 0.2])],
            # 26
            [pyrr.Vector3([25.88, 1.2, -23.5]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([0.2, 0.2, 0.2])],

            # 27

            # 20
            [pyrr.Vector3([19.12, 1.2, -24.5]), pyrr.Vector3([0., 180., 0.]), pyrr.Vector3([0.2, 0.2, 0.2])],

            # 29

            # 2
            [pyrr.Vector3([1.5, 1.2, -26.88]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([0.2, 0.2, 0.2])],
            # 14
            [pyrr.Vector3([13.5, 1.2, -26.12]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([0.2, 0.2, 0.2])],
            # 23
            [pyrr.Vector3([22.88, 1.2, -26.5]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([0.2, 0.2, 0.2])],
            # 28
            [pyrr.Vector3([27.5, 1.2, -26.88]), pyrr.Vector3([0., -90., 0.]), pyrr.Vector3([0.2, 0.2, 0.2])],

        ])
        for coords in self.torch_coords:
            new_actor = actor.Actor(
                    sp.Spawnpoint(*coords), self.torch_model
                )
            self.torches.append(new_actor)
        model_identity = pyrr.Matrix44.identity()
        model_matrices = list()
        for torch in self.torches:
            model_inst = model_identity * torch.get_model_matrix()
            model_matrices.append(model_inst)
        model_matrices = numpy.array(model_matrices, dtype=numpy.float32)

        self.torch_model.prepare_instanced_draw(model_matrices)

    def load_fires(self):
        self.fire_model = model.Model("resources/sprite/sprite.obj",
                                      "resources/sprite/fire.mtl")
        self.fire_coords = numpy.array([
            # 2

            # 2
            [pyrr.Vector3([1.16, 1.5, 0.5]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([0.2, 0.2, 0.2])],
            # 11
            [pyrr.Vector3([10.5, 1.5, 0.83]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([0.2, 0.2, 0.2])],
            # 17
            [pyrr.Vector3([16.84, 1.5, 0.5]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([0.2, 0.2, 0.2])],
            # 23
            [pyrr.Vector3([22.5, 1.5, 0.83]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([0.2, 0.2, 0.2])],

            # 5

            # 8
            [pyrr.Vector3([7.84, 1.5, -2.5]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([0.2, 0.2, 0.2])],
            # 13
            [pyrr.Vector3([12.5, 1.5, -2.83]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([0.2, 0.2, 0.2])],
            # 20
            [pyrr.Vector3([19.5, 1.5, -2.83]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([0.2, 0.2, 0.2])],
            # 29
            [pyrr.Vector3([28.84, 1.5, -2.5]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([0.2, 0.2, 0.2])],

            # 8

            # 2
            [pyrr.Vector3([1.16, 1.5, -5.5]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([0.2, 0.2, 0.2])],
            # 10
            [pyrr.Vector3([9.5, 1.5, -5.17]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([0.2, 0.2, 0.2])],
            # 14
            [pyrr.Vector3([13.16, 1.5, -5.5]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([0.2, 0.2, 0.2])],
            # 26
            [pyrr.Vector3([25.5, 1.5, -5.83]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([0.2, 0.2, 0.2])],

            # 11

            # 5
            [pyrr.Vector3([4.84, 1.5, -8.5]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([0.2, 0.2, 0.2])],
            # 20
            [pyrr.Vector3([19.84, 1.5, -8.5]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([0.2, 0.2, 0.2])],
            # 23
            [pyrr.Vector3([22.16, 1.5, -8.5]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([0.2, 0.2, 0.2])],
            # 29
            [pyrr.Vector3([28.84, 1.5, -8.5]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([0.2, 0.2, 0.2])],

            # 14

            # 2
            [pyrr.Vector3([1.5, 1.5, -11.17]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([0.2, 0.2, 0.2])],
            # 11
            [pyrr.Vector3([10.5, 1.5, -11.83]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([0.2, 0.2, 0.2])],
            # 20
            [pyrr.Vector3([19.5, 1.5, -11.17]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([0.2, 0.2, 0.2])],
            # 26
            [pyrr.Vector3([25.5, 1.5, -11.83]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([0.2, 0.2, 0.2])],

            # 15

            # 17
            [pyrr.Vector3([16.16, 1.5, -12.5]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([0.2, 0.2, 0.2])],

            # 17

            # 8
            [pyrr.Vector3([7.16, 1.5, -14.5]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([0.2, 0.2, 0.2])],
            # 26
            [pyrr.Vector3([25.84, 1.5, -14.5]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([0.2, 0.2, 0.2])],

            # 20

            # 5
            [pyrr.Vector3([4.16, 1.5, -17.5]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([0.2, 0.2, 0.2])],
            # 14
            [pyrr.Vector3([13.16, 1.5, -17.5]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([0.2, 0.2, 0.2])],
            # 20
            [pyrr.Vector3([19.5, 1.5, -17.17]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([0.2, 0.2, 0.2])],
            # 29
            [pyrr.Vector3([28.5, 1.5, -17.83]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([0.2, 0.2, 0.2])],

            # 21

            # 2
            [pyrr.Vector3([1.16, 1.5, -18.5]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([0.2, 0.2, 0.2])],

            # 23

            # 11
            [pyrr.Vector3([10.84, 1.5, -20.5]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([0.2, 0.2, 0.2])],
            # 17
            [pyrr.Vector3([16.84, 1.5, -20.5]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([0.2, 0.2, 0.2])],
            # 23
            [pyrr.Vector3([22.5, 1.5, -20.83]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([0.2, 0.2, 0.2])],
            # 29
            [pyrr.Vector3([28.5, 1.5, -20.17]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([0.2, 0.2, 0.2])],

            # 26

            # 8
            [pyrr.Vector3([7.84, 1.5, -23.5]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([0.2, 0.2, 0.2])],
            # 13
            [pyrr.Vector3([12.5, 1.5, -23.83]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([0.2, 0.2, 0.2])],
            # 26
            [pyrr.Vector3([25.84, 1.5, -23.5]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([0.2, 0.2, 0.2])],

            # 27

            # 20
            [pyrr.Vector3([19.16, 1.5, -24.5]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([0.2, 0.2, 0.2])],

            # 29

            # 2
            [pyrr.Vector3([1.5, 1.5, -26.83]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([0.2, 0.2, 0.2])],
            # 14
            [pyrr.Vector3([13.5, 1.5, -26.17]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([0.2, 0.2, 0.2])],
            # 23
            [pyrr.Vector3([22.84, 1.5, -26.5]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([0.2, 0.2, 0.2])],
            # 28
            [pyrr.Vector3([27.5, 1.5, -26.83]), pyrr.Vector3([0., 90., 0.]), pyrr.Vector3([0.2, 0.2, 0.2])],
        ])
        for coords in self.fire_coords:
            new_anim_actor = aa.AnimActor(
                sp.Spawnpoint(*coords), self.fire_model
            )
            new_anim_actor.create_sprite_animator(rows=6, columns=8)
            self.fires.append(
                new_anim_actor
            )
        model_identity = pyrr.Matrix44.identity()
        model_matrices = list()
        for fire in self.fires:
            model_inst = model_identity * fire.get_model_matrix()
            model_matrices.append(model_inst)
        model_matrices = numpy.array(model_matrices, dtype=numpy.float32)

        self.fire_model.prepare_instanced_draw(model_matrices)

    def load_exit_sprite(self):
        self.exit_sprite_model = model.Model("resources/sprite/sprite.obj",
                                      "resources/sprite/exit_sprite.mtl")
        self.exit_sprite_coords = numpy.array([
            [pyrr.Vector3([13.5, 1.25, -27.99]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([0.5, 0.25, 0.5])]
        ])
        for coords in self.exit_sprite_coords:
            new_actor = actor.Actor(
                sp.Spawnpoint(*coords), self.exit_sprite_model
            )
            self.exit_sprites.append(
                new_actor
            )
        model_identity = pyrr.Matrix44.identity()
        model_matrices = list()
        for exit_sprite in self.exit_sprites:
            model_inst = model_identity * exit_sprite.get_model_matrix()
            model_matrices.append(model_inst)
        model_matrices = numpy.array(model_matrices, dtype=numpy.float32)

        self.exit_sprite_model.prepare_instanced_draw(model_matrices)

    def load_mem(self):
        self.mem_model = model.Model("resources/sprite/sprite.obj",
                                      "resources/sprite/mem.mtl")
        self.mem_coords = numpy.array([
            [pyrr.Vector3([13.5, 0.7, -27.98]), pyrr.Vector3([0., 0., 0.]), pyrr.Vector3([0.25, 0.25, 0.25])]
        ])
        for coords in self.mem_coords:
            new_actor = aa.AnimActor(
                sp.Spawnpoint(*coords), self.mem_model
            )
            new_actor.create_sprite_animator(rows=8, columns=5, time=2)
            self.mems.append(
                new_actor
            )
        model_identity = pyrr.Matrix44.identity()
        model_matrices = list()
        for mem in self.mems:
            model_inst = model_identity * mem.get_model_matrix()
            model_matrices.append(model_inst)
        model_matrices = numpy.array(model_matrices, dtype=numpy.float32)

        self.mem_model.prepare_instanced_draw(model_matrices)

    def load_exit_trigger(self):
        exit_trigger_coord = [pyrr.Vector3([13.5, 0.2, -27.5]), pyrr.Vector3([0., 0, 0.]), pyrr.Vector3([0.5, 1., 0.5])]
        self.exit_trigger = actor.Actor(sp.Spawnpoint(*exit_trigger_coord), self.floor_rectangle_model)

    def draw(self):
        self.prepare()
        self.draw_skybox()
        self.draw_walls()
        self.draw_wall_corner_out()
        self.draw_floors()
        self.draw_floor_rectangles()
        self.draw_torches()
        self.draw_fire()
        self.draw_exit_sprite()
        self.draw_mem()

    def prepare(self):
        self.view = game.Game.character.camera.get_view_matrix()
        self.projection = pyrr.Matrix44.perspective_projection(
            game.Game.character.camera.zoom, game.Game.main_window.aspect_ratio, 0.01, 200.0)
        game.Game.shaders["ads"].use()
        game.Game.shaders["ads"].set_mat4("view", self.view)
        game.Game.shaders["ads"].set_mat4("projection", self.projection)
        game.Game.shaders["fire"].use()
        game.Game.shaders["fire"].set_mat4("view", self.view)
        game.Game.shaders["fire"].set_mat4("projection", self.projection)

    def draw_skybox(self):
        glDepthMask(GL_FALSE)
        game.Game.shaders["ads"].use()
        self.skybox_model.set_shader(game.Game.shaders["ads"])
        self.skybox_model.draw_instanced(len(self.skyboxes))
        glDepthMask(GL_TRUE)

    def draw_walls(self):
        game.Game.shaders["ads"].use()
        self.wall_model.set_shader(game.Game.shaders["ads"])
        self.wall_model.draw_instanced(len(self.walls))

    def draw_wall_corner_out(self):
        game.Game.shaders["ads"].use()
        self.wall_corner_out_model.set_shader(game.Game.shaders["ads"])
        self.wall_corner_out_model.draw_instanced(len(self.wall_corner_out))

    def draw_floors(self):
        game.Game.shaders["ads"].use()
        self.floor_model.set_shader(game.Game.shaders["ads"])
        self.floor_model.draw_instanced(len(self.floors))

    def draw_floor_rectangles(self):
        game.Game.shaders["ads"].use()
        self.floor_rectangle_model.set_shader(game.Game.shaders["ads"])
        self.floor_rectangle_model.draw_instanced(len(self.floor_rectangles))

    def draw_torches(self):
        game.Game.shaders["ads"].use()
        self.torch_model.set_shader(game.Game.shaders["ads"])
        self.torch_model.draw_instanced(len(self.torches))

    def draw_fire(self):
        glDisable(GL_CULL_FACE)
        game.Game.shaders["fire"].use()
        self.fire_model.set_shader(game.Game.shaders["fire"])
        self.fires[0].sprite_anim_next_frame()
        model_identity = pyrr.Matrix44.identity()
        model_matrices = list()
        for fire in self.fires:
            fire.link_to_actor(game.Game.character.camera)
            model_inst = model_identity * fire.get_model_matrix()
            model_matrices.append(model_inst)
        model_matrices = numpy.array(model_matrices, dtype=numpy.float32)
        for i in range(len(self.fire_model.meshes)):
            glBindBuffer(GL_ARRAY_BUFFER, self.fire_model.meshes[i].instanced_buffer)
            glBufferData(GL_ARRAY_BUFFER, len(model_matrices) * 16 * 4, model_matrices, GL_DYNAMIC_DRAW)
        self.fire_model.draw_instanced(len(self.fires))
        glEnable(GL_CULL_FACE)
        glFrontFace(GL_CCW)

    def draw_exit_sprite(self):
        game.Game.shaders["ads"].use()
        self.exit_sprite_model.set_shader(game.Game.shaders["ads"])
        self.exit_sprite_model.draw_instanced(len(self.exit_sprites))

    def draw_mem(self):
        game.Game.shaders["ads"].use()
        self.mem_model.set_shader(game.Game.shaders["ads"])
        self.mems[0].sprite_anim_next_frame()
        self.mem_model.draw_instanced(len(self.mems))
