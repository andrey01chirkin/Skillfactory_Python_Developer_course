from data import students, students_marks


def output_marks_by_student():
    print('5. Вывод информации по всем оценкам для определенного ученика.')
    student = input("Введите имя ученика: ")
    if student in students:
        for class_, marks in students_marks[student].items():
            print(f"{class_} - {marks}")
    else:
        print('ОШИБКА: неверное имя ученика')