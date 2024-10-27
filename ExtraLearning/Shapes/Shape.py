from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, x, y, color = "Black"):
        self.x = x
        self.y = y
        self.color = color

    def get_color(self):
        return self.color

    @abstractmethod
    def draw(self):
        pass