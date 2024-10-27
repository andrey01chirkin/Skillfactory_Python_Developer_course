from abc import ABC, abstractmethod

class Function:
    def __init__(self):
        self.__x = None
        self.__y = None

    @abstractmethod
    def calculate(self, x):
        pass

    @abstractmethod
    def print_data(self):
        pass
