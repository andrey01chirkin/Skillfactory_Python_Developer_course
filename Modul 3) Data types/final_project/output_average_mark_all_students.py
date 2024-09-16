from data import *


def output_average_mark_all_students():
    print('2. Вывести средний балл по всем предметам по каждому ученику')
    # цикл по ученикам
    for student in students:
        print(student)
        # цикл по предметам
        for class_ in classes:
            # находим сумму оценок по предмету
            marks_sum = sum(students_marks[student][class_])
            # находим количество оценок по предмету
            marks_count = len(students_marks[student][class_])
            # выводим средний балл по предмету
            print(f'{class_} - {marks_sum // marks_count}')
        print()