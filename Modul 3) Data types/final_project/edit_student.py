from data import students_marks, classes, students


def edit_student():
    print('12. Отредактировать имя студента')
    name_old = input("Введите имя студента для редактирования: ")
    name_new = input("Введите новое имя студента: ")
    if name_old in students:
        students_marks[name_new] = students_marks[name_old].copy()
        students_marks.pop(name_old)
        students[students.index(name_old)] = name_new
        print(f"Имя студента \"{name_old}\" изменено на \"{name_new}\"")
    else:
        print('ОШИБКА: неверное имя студента')