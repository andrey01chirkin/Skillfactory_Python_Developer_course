from Shape import Shape


class Point(Shape):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)

    def draw(self):
        print(f"Point {self.x} {self.y} {self.get_color()}")