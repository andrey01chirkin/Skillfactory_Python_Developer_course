from pprint import pprint

class Coords:
    min = 10
    max = 20

    @classmethod
    def __check_value(cls, num):
        return cls.min < num < cls.max

    def __init__(self, __x, __y):
        print(self.min, self.max)
        self.__x = self.__y = 0
        if self.__check_value(__x) and self.__check_value(__y):
            self.__x = __x
            self.__y = __y

    def get_coord(self):
        return self.__x, self.__y

    @staticmethod
    def calculate(__x, __y):
        return __x*__y

c = Coords(15, 17)
print(Coords.calculate(10, 5))

pprint(c.__)