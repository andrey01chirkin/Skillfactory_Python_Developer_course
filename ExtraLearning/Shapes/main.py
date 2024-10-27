import os
import sys
from pprint import pprint


class NonPositiveDigitException(ValueError):
    pass

class Square:
    def __init__(self, a):
        if a <= 0:
            raise NonPositiveDigitException("Сторона квадрата меньше или равна 0")

if __name__ == "__main__":
    #Square(-15)
    pprint(sys.path)




# if __name__ == "__main__":
#     pc = Circle(10, 15, 30, "Blue")
#     pp = Point(10, 15, "Yellow")
#
#     sc = Scene()
#     sc.add(pc)
#     sc.add(pp)
#     sc.show_data()
#     sc.scale_data()
#     print()
#     sc.show_data()