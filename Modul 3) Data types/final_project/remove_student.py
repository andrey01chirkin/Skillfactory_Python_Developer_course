from data import students_marks, students


def remove_student():
    print('11. Удалить студента')
    student = input("Введите имя студента: ")
    if student in students:
        for student in students_marks.keys():
            students_marks.pop(student)
        students.remove(student)
        print(f"Студента \"{student}\" удален")
    else:
        print('ОШИБКА: неверное имя ученика')