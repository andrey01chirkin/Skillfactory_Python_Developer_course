from Transport import Transport


class Motorbike(Transport):

    def __init__(self, mark, number, speed, load_capacity, has_stroller):
        super().__init__(mark, number, speed, load_capacity, has_stroller)
        self.__has_stroller = has_stroller

    def printData(self):
        print(f"\n---Motorbike---\nmark:{self._mark}\nnumber:{self._number}\nspeed:{self._speed}\nload capacity:{self._load_capacity}\nhas stroller: {self.__has_stroller}")




