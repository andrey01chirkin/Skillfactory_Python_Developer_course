
'''
При дальнейшей разработке платформы онлайн-школы вам поручили дополнить логику программы возможностью объединения
студентов в группы.
Для этого объявите класс Group с атрибутом members, который ссылается на пустой список.
Также объявите класс Student и создайте студента s1 в соответствии с предыдущим заданием. Далее создайте студента s2
(значения атрибутов можете выбрать сами, имена атрибутов — такие же, как и у студента s1).
После этого обратитесь к значению атрибута members класса Group и добавьте в список объекты s1 и s2.
Запишите в переменную result значение атрибута members класса Group.
'''
from enum import member


class Group:
    members = []

class Student:
    course = "Data Science"

s1 = Student()

setattr(s1, 'name', 'Иван')
setattr(s1, 'surname', 'Иванов')
setattr(s1, 'semester', 1)

s2 = Student()

setattr(s2, 'name', 'Лев')
setattr(s2, 'surname', 'Сергеев')
setattr(s2, 'semester', 1)

getattr(Group, 'members').append(s1)
getattr(Group, 'members').append(s2)

result = getattr(Group, 'members')

print(result)
