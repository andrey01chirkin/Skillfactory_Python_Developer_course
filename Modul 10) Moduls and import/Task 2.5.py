
class NonPositiveDigitException(ValueError):
    pass

class Square:
    def __init__(self, a):
        if a <= 0:
            raise NonPositiveDigitException('Сторона квадрата меньше 0')

Square(5)
