import pyrr


class Spawnpoint:
    def __init__(self, position: pyrr.Vector3, rotation: pyrr.Vector3, scale: pyrr.Vector3):
        self.position = position
        self.rotation = rotation
        self.scale = scale