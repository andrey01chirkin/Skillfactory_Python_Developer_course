
'''
Определите класс IntDataFrame, который в момент инициализации объектов принимает список неотрицательных чисел и
приводит к целым значениям все числа в этом списке, отрезая дробную часть с помощью встроенной функции int().

Результирующий список должен быть сохранен в виде атрибута с именем column.

Также класс должен содержать следующие методы:
count(), который возвращает количество ненулевых элементов в списке column;
unique(), который возвращает число уникальных элементов в списке в списке column.

В случае правильного описания класса код, приведённый ниже, должен выдать следующий результат:

Пример использования класса:

df = IntDataFrame([4.7, 4, 3, 0, 2.4, 0.3, 4])

print(df.column)
# [4, 4, 3, 0, 2, 0, 4]

print(df.count())
# 5

print(df.unique())
# 4
'''
from itertools import count


class IntDataFrame:
    def __init__(self, list_numbers):
        self.column = list(map(lambda number: int(number), list_numbers))

    def count(self):
        return len(list(filter(lambda num: num > 0, self.column)))

    def unique(self):
        return len(set(self.column))

df = IntDataFrame([4.7, 4, 3, 0, 2.4, 0.3, 4])

print(df.column)
# [4, 4, 3, 0, 2, 0, 4]

print(df.count())
# 5

print(df.unique())
# 4


