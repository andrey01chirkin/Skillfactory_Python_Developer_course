
from pprint import pprint

'''
При разработке платформы онлайн-школы вам поручили реализовать класс Student c атрибутом course. Значение атрибута — "Data Science".
После объявления класса создайте экземпляр класса s1 и добавьте ему локальные атрибуты:

name со значением "Иван";
surname со значением "Иванов";
semester со значением 1.
Запишите в переменную result локальные атрибуты (как служебные, так и пользовательские) экземпляра s1 в виде словаря.
'''

class Student:
    course = "Data Science"

s1 = Student()

setattr(s1, 'name', 'Иван')
setattr(s1, 'surname', 'Иванов')
setattr(s1, 'semester', 1)

result = s1.__dict__

print(result)


