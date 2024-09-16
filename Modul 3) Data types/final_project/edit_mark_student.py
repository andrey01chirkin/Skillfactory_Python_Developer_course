from data import *


def edit_mark_student():
    print('8. Отредактировать оценку студента')
    student = input("Введите имя студента: ")
    class_ = input("Введите название предмета: ")
    mark_old = int(input("Введите оценку для редактирования: "))
    mark_new = int(input("Введите новую оценку: "))
    if student in students and class_ in classes and mark_old in students_marks[student][class_]:
        index_mark_old = students_marks[student][class_].index(mark_old)
        students_marks[student][class_][index_mark_old] = mark_new
        print(f"Оценка {mark_old} у студента {student} изменна на {mark_new}")
    else:
        print('ОШИБКА: неверное имя ученика или название предмета или оценка')