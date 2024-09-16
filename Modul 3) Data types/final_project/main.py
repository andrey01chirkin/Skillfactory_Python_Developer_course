from add_marks import add_marks
from output_average_mark_all_students import output_average_mark_all_students
from output_marks_all_students import output_marks_all_students
from output_marks_by_student import output_marks_by_student
from output_average_mark_by_student import output_average_mark_by_student
from remove_mark_student import remove_mark_student
from edit_mark_student import edit_mark_student
from remove_class import remove_class
from edit_class import edit_class
from edit_student import edit_student
from remove_student import remove_student
from initialization import initialization


def main():
    initialization()
    print('''
            Список команд:
            1. Добавить оценку ученика по предмету
            2. Вывести средний балл по всем предметам по каждому ученику
            3. Вывести все оценки по всем ученикам
            4. Выход из программы
            5. Вывести информацию по всем оценкам для определенного ученика
            6. Вывести средний балл по каждому предмету по определенному ученику
            7. Удалить оценку у студента
            8. Редактировать оценку у студента
            9. Удалить предмет у студентов
            10. Отредактировать наименование предмета
            11. Удалить студента
            12. Отредактировать имя студента
        ''')

    while True:
        command = int(input('Введите команду: '))
        if command == 1:
            add_marks()
        elif command == 2:
            output_average_mark_all_students()
        elif command == 3:
            output_marks_all_students()
        elif command == 4:
            print('4. Выход из программы')
            break
        elif command == 5:
            output_marks_by_student()
        elif command == 6:
            output_average_mark_by_student()
        elif command == 7:
            remove_mark_student()
        elif command == 8:
            edit_mark_student()
        elif command == 9:
            remove_class()
        elif command == 10:
            edit_class()
        elif command == 11:
            remove_student()
        elif command == 12:
            edit_student()


if __name__ == "__main__":
    main()