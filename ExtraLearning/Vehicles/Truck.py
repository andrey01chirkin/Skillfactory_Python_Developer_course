from Transport import Transport


class Truck(Transport):
    def __init__(self, mark, number, speed, load_capacity, has_trailer):
        super().__init__(mark, number, speed, load_capacity, has_trailer)
        self.__has_trailer = has_trailer

    def printData(self):
        print(f"\n---Truck---\nmark: {self._mark}\nnumber: {self._number}\nspeed: {self._speed}\nload capacity: {self._load_capacity}\nhas trailer: {self.__has_trailer}")