from Function import Function


class Kub(Function):
    def __init__(self, a, b, c):
        super().__init__()
        self.__a = a
        self.__b = b
        self.__c = c


    def calculate(self, x):
        self.__x = x
        self.__y = self.__a*self.__x**2 + self.__b*x + self.__c

    def print_data(self):
        print(f"Kub: {self.__a} * {self.__x**2} + {self.__b} * {self.__x} + {self.__c} = {self.__y}")