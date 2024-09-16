from data import students_marks, classes


def remove_class():
    print('9. Удалить предмет у студентов')
    class_ = input("Введите название предмета для удаления: ")
    if class_ in classes:
        for student in students_marks.keys():
            students_marks[student].pop(class_)
        classes.remove(class_)
        print(f"Предмет \"{class_}\" удален")
    else:
        print('ОШИБКА: неверное название предмета')