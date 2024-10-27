from Function import Function


class Hyperbola(Function):
    def __init__(self, a):
        super().__init__()
        self.__a = a

    def calculate(self, x):
        self.__x = x

        if self.__x == 0:
            raise ZeroDivisionError("На ноль делить нельзя")

        self.__y = self.__a / self.__x


    def print_data(self):
        print(f"Hyperbola: {self.__a} / {self.__x} = {self.__y}")