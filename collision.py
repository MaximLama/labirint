class Collision:
    def __init__(self, min_point, max_point):
        self.front_line = None
        self.back_line = None
        self.left_line = None
        self.right_line = None
        self.min = min_point
        self.max = max_point
        self.get_proj_lines()

    def get_line(self, side: str):
        if side == "front":
            return self.front_line
        if side == "back":
            return self.back_line
        if side == "left":
            return self.left_line
        if side == "right":
            return self.right_line

    def get_proj_lines(self):
        self.front_line = [
            [self.min[0], self.max[2]],
            [self.max[0], self.max[2]]
        ]
        self.back_line = [
            [self.min[0], self.min[2]],
            [self.max[0], self.min[2]]
        ]
        self.left_line = [
            [self.min[0], self.min[2]],
            [self.min[0], self.max[2]]
        ]
        self.right_line = [
            [self.max[0], self.min[2]],
            [self.max[0], self.max[2]]
        ]