from Hyperbola import Hyperbola
from Kub import Kub
from Line import Line

if __name__ == "__main__":
    h = Hyperbola(5)
    h.calculate(2)

    k = Kub(5, 10, 15)
    k.calculate(20)

    l = Line(5, 10)
    l.calculate(15)

    lst = [h, k, l]
    for obj in lst:
        obj.print_data()


