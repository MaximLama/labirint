class SpriteAnimator:
    def __init__(self, rows, columns, time):
        self.current_frame = 0
        self.rows = rows
        self.columns = columns
        self.time_frame = 0
        self.time = time
