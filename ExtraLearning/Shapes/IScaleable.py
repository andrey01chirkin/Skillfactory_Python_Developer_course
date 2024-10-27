from abc import ABC, abstractmethod

class IScaleable(ABC):
    @abstractmethod
    def scale(self):
        pass

