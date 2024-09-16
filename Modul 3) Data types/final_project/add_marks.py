from data import students_marks


def add_marks():
    print('1. Добавить оценку ученика по предмету')
    # считываем имя ученика
    student = input('Введите имя ученика: ')
    # считываем название предмета
    class_ = input('Введите предмет: ')
    # считываем оценку
    mark = int(input('Введите оценку: '))
    # если данные введены верно
    if student in students_marks.keys() and class_ in students_marks[student].keys():
        # добавляем новую оценку для ученика по предмету
        students_marks[student][class_].append(mark)
        print(f'Для {student} по предмету {class_} добавлена оценка {mark}')
    # неверно введены название предмета или имя ученика
    else:
        print('ОШИБКА: неверное имя ученика или название предмета')
