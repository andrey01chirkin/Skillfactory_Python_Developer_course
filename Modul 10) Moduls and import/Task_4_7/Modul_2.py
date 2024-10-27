from Modul_1 import *

def main():
    r_circle = int(input("Введите площадь круга: "))
    a_rect = int(input("Введите первую сторону прямоугольника: "))
    b_rect = int(input("Введите вторую сторону прямоугольника: "))

    if circle_area(r_circle) > rect_area(a_rect, b_rect):
        print('Площадь круга больше')
    else:
        print('Площадь прямоугольника больше')


if __name__ == "__main__":
    main()





