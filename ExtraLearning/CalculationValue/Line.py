from Function import Function

class Line(Function):
    def __init__(self, a, b):
        super().__init__()
        self.__a = a
        self.__b = b

    def calculate(self, x):
        self.__x = x
        self.__y = self.__a * self.__x + self.__b

    def print_data(self):
        print(f"Line: {self.__a} * {self.__x} + {self.__b} = {self.__y}")