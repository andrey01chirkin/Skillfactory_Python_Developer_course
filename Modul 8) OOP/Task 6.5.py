
'''
При разработке графического редактора вам поручили реализовать класс Triangle, в котором инициализатор создает локальные атрибуты a, b, c — длины сторон треугольника.
Добавьте методы:
- is_triangle(), который возвращает True, если такой треугольник может существовать (если каждая сторона треугольника меньше суммы двух других сторон, значит, треугольник существует), и False — в противном случае.
- get_triangle_area(), который возвращает площадь треугольника (формула Герона), но только если такой треугольник существует. Иначе метод должен возвращать значение 0.

Пример использования класса Triangle:

t1 = Triangle(a=3, b=4, c=5)
print(t1.is_triangle())

# True

print(t1.get_triangle_area())

# 6.0

t2 = Triangle(a=10, b=5, c=5)
print(t2.is_triangle())

# False
'''

class Triangle:
    def __init__(self,a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        return self.a < self.b + self.c and self.b < self.a + self.c and self.c < self.a + self.b

    def get_triangle_area(self):
        p = (self.a + self.b + self.c) / 2
        return pow(p*(p-self.a)*(p-self.b)*(p-self.c), 0.5) if self.is_triangle() else 0

t1 = Triangle(a=3, b=4, c=5)
print(t1.is_triangle())

# True

print(t1.get_triangle_area())

# 6.0

t2 = Triangle(a=10, b=5, c=5)
print(t2.is_triangle())

# False
