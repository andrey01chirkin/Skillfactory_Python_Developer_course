from random import randint
from data import *


def initialization():
    for student in students:  # 1 итерация: student = 'Александра'
        students_marks[student] = {}  # 1 итерация: students_marks['Александра'] = {}
        # цикл по предметам
        for class_ in classes:  # 1 итерация: class_ = 'Математика'
            marks = [randint(1, 5) for i in range(3)]  # генерируем список из 3х случайных оценок
            students_marks[student][class_] = marks  # students_marks['Александра']['Математика'] = [5, 5, 5]
    # выводим получившийся словарь с оценками:
    for student in students:
        print(f'''{student}
                {students_marks[student]}''')