from data import *


def output_marks_all_students():
    print('3. Вывести все оценки по всем ученикам')
    # выводим словарь с оценками:
    # цикл по ученикам
    for student in students:
        print(student)
        # цикл по предметам
        for class_ in classes:
            print(f'\t{class_} - {students_marks[student][class_]}')
        print()
