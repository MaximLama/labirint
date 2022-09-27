import pyrr
import collision as c


class CollisionProjection(c.Collision):
    def __init__(self, min_point, max_point, matrix_model):
        super().__init__(min_point, max_point)
        self.matrix_model = matrix_model
        self.transform_collision_projection()

    def transform_collision_projection(self):
        self.front_line[0] = self.transform_point(self.front_line[0])
        self.front_line[1] = self.transform_point(self.front_line[1])
        self.back_line[0] = self.transform_point(self.back_line[0])
        self.back_line[1] = self.transform_point(self.back_line[1])
        self.left_line[0] = self.transform_point(self.left_line[0])
        self.left_line[1] = self.transform_point(self.left_line[1])
        self.right_line[0] = self.transform_point(self.right_line[0])
        self.right_line[1] = self.transform_point(self.right_line[1])

    def transform_point(self, point):
        point_v4 = self.matrix_model * pyrr.Vector4([point[0], 0, point[1], 1])
        return [point_v4[0], point_v4[2]]

    def change_projection(self, matrix_model):
        self.matrix_model = matrix_model
        self.get_proj_lines()
        self.transform_collision_projection()
