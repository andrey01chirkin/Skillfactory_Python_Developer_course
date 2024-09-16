from data import students_marks, students


def output_average_mark_by_student():
    print('6. Вывод среднего балла по каждому предмету по определенному ученику.')
    student = input("Введите имя ученика: ")
    if student in students:
        for class_, marks in students_marks[student].items():
            print(f"Средний бал по {class_} = {sum(marks) // len(marks)}")
    else:
        print('ОШИБКА: неверное имя ученика')




