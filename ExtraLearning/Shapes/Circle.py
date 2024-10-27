from IScaleable import IScaleable
from Shape import Shape

class Circle(Shape, IScaleable):
    def __init__(self, x, y, r, color):
        super().__init__(x, y, color)
        self.r = r

    def draw(self):
        print(f"Circle {self.x} {self.y} {self.r} {self.get_color()}")

    def scale(self):
        self.x *= 10
        self.y *= 10
        self.r *= 10