
numbers_list = [1,2,3]
extra_numbers = [4,5,6,7]
numbers_list.insert(2, 0)

print(numbers_list)
numbers_list.sort(reverse=True)
print(numbers_list)

#Пусть пользователь заполняет ежедневник делами на день. Затем редактирует информацию
# для первой записи, удаляет последнюю запись и выводит список дел по порядку.

todo_list = list()

stop = False
while not stop:
    task = input("Введите дело, чтобы сделать: ")
    if not task == "-1":
        todo_list.append(task)
    else:
        stop = True

print("Список дел на сегодня: \n", todo_list)

number_task = int(input("Введите номер дела, которое нужно отредактировать: "))
if (number_task-1) < (len(todo_list)-1):
    description_task = input("Введите описание задачи: ")
    todo_list[number_task-1] = description_task

print(todo_list)

task_remove_index = int(input("Введите индекс дела, которое нужно удалить: "))
if task_remove_index < (len(todo_list)-1):
    todo_list.pop(task_remove_index)

print(todo_list)