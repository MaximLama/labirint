import copy


class Physics:

    @classmethod
    def get_new_position(cls, walls, position, possible_position):

        if Physics.check_intersection(walls, position, possible_position):
            new_position_x = copy.deepcopy(possible_position)
            new_position_x[0] = position[0]
            new_position_z = copy.deepcopy(possible_position)
            new_position_z[2] = position[2]
            # можно ли двигаться по z
            if not Physics.check_intersection(walls, position, new_position_x):
                return new_position_x
            # можно ли двигаться по x
            if not Physics.check_intersection(walls, position, new_position_z):
                return new_position_z
            new_position_x_z = possible_position
            new_position_x_z[0] = position[0]
            new_position_x_z[2] = position[2]
            return new_position_x_z
        else:
            return possible_position


    @classmethod
    def check_intersection(cls, walls, position, new_position):
        q1 = [position[0], position[2]]
        q2 = [new_position[0], new_position[2]]
        for wall in walls:
            if abs(wall.position[0] - position[0]) <= 2 and abs(wall.position[2]-position[2]) <= 2:
                line_names = ["front", "back", "left", "right"]
                for line_name in line_names:
                    line = wall.collision_projection.get_line(line_name)
                    p1 = line[0]
                    p2 = line[1]
                    if Physics.check_intersect_dimension(
                        p1[0], p2[0], q1[0], q2[0]
                    ) and Physics.check_intersect_dimension(
                        p1[1], p2[1], q1[1], q2[1]
                    ) and Physics.area(p1, p2, q1) * Physics.area(p1, p2, q2) <= 0\
                            and Physics.area(q1, q2, p1) * Physics.area(q1, q2, p2) <= 0:
                        return True
        return False
    @classmethod
    def check_intersect_dimension(cls, p1, p2, q1, q2):
        if p1 > p2:
            p1, p2 = p2, p1
        if q1 > q2:
            q1, q2 = q2, q1
        return max(p1, q1) <= min(p2, q2)

    @classmethod
    def area(cls, a, b, c):
        return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
