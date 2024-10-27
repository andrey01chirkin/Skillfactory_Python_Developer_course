from Circle import Circle
from Point import Point

class Scene:
    def __init__(self):
        self.scene = []

    def add(self, obj:object):
        self.scene.append(obj)

    def show_data(self):
        for obj in self.scene:
            if isinstance(obj, Circle | Point):
                obj.draw()

    def scale_data(self):
        for obj in self.scene:
            if isinstance(obj, Circle):
                obj.scale()