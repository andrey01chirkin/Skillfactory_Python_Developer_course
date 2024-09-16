from data import *


def remove_mark_student():
    print('7. Удалить оценку у студента')
    student = input("Введите имя студента: ")
    class_ = input("Введите название предмета: ")
    mark = int(input("Введите оценку для удаления: "))
    if student in students and class_ in classes and mark in students_marks[student][class_]:
        students_marks[student][class_].remove(mark)
        print(f"У студента \"{student}\" удалена оценка {mark}")
    else:
        print('ОШИБКА: неверное имя ученика или название предмета или оценка')