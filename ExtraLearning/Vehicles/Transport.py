from abc import ABC, abstractmethod
from accessify import protected, private

class Transport(ABC):
    def __init__(self, mark, number, speed, load_capacity, has_stroller=None, has_trailer=None):
        self._mark = mark
        self._number = number
        self._speed = speed
        self._load_capacity = None
        self.__calculateLoadCapacity(load_capacity, has_stroller, has_trailer)

    @property
    def load_capacity(self):
        return self._load_capacity

    def printData(self):
        print(f"\n---Car---\nmark: {self._mark}\nnumber: {self._number}\nspeed: {self._speed}\nload_capacity: {self._load_capacity}")

    def __calculateLoadCapacity(self, load_capacity, has_stroller, has_trailer):
        if has_stroller == False:
            self._load_capacity = 0
            return
        if has_trailer:
            self._load_capacity = load_capacity * 2
            return
        self._load_capacity = load_capacity


    @staticmethod
    def CompareTo(vehicles: list):
        vehicles.sort(key=lambda vehicle: vehicle.load_capacity)

    @staticmethod
    def searchVehicleByLoadCapacity(vehicles: list, min_requirement):
        for vehicle in vehicles:
            if vehicle.load_capacity >= min_requirement:
                vehicle.printData()
