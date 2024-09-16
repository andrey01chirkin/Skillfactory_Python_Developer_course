from data import students_marks, classes


def edit_class():
    print('10. Отредактировать наименование предмета')
    class_old = input("Введите название предмета для редактирования: ")
    class_new = input("Введите новок название предмета: ")
    if class_old in classes:
        for student in students_marks.keys():
            students_marks[student][class_new] = students_marks[student][class_old].copy()
            students_marks[student].pop(class_old)
        classes[classes.index(class_old)] = class_new
        print(f"Предмет \"{class_old}\" изменен на \"{class_new}\"")
    else:
        print('ОШИБКА: неверное название предмета')