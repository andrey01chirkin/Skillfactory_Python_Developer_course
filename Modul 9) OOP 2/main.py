class Parent:
    def __init__(self, a, b):
        self.a = a
        self.b = b

class Child(Parent):
    def __init__(self, a, b, c):
        super().__init__(a, b)
        self.c = c

child = Child(1,2,3)

print(child.a)
print(child.b)
print(child.c)


class Shape:
    def __init__(self, color="Black"):
        self.color = color

    def draw(self):
        print("Class Shape")


class Point(Shape):
    def __init__(self, x, y, color="Blue"):
        super().__init__(color)
        self.x = x
        self.y = y

    def draw(self):
        print(self.x, self.y)

class Circle(Shape):
    def __init__(self, x, y, r, color):
        super().__init__(color)
        self.__x = x
        self._y = y
        self.r = r


c = Circle(10, 15, 20,"Yellow")
p = Point(17, 20)
print(dir(c))




