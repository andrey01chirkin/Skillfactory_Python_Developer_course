
todo_list = []

rows = 7
columns = 3

for i in range(rows):
    todo_list.append(['']*columns)

print(todo_list)

days = ("Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье")
time_interval = ("Утро", "День", "Вечер")

for i in range(rows):
    for j in range(columns):
        print(f"День: {days[i]} || Интервал времени:{time_interval[j]}")
        todo_list[i][j] = input("Введите дело: ")

print(todo_list)

print("\nУдаление записи")
index_day = int(input("Введите индекс дня недели: "))
index_time_interval = int(input("Введите индекс временного интервала: "))
todo_list[index_day].pop(index_time_interval)

print(todo_list)

print("\nДобавление элемента")
index_day = int(input("Введите индекс дня недели: "))
new_task = input("Введите новую запись: ")
todo_list[index_day].append(new_task)

print("\nВывод данных")
for i in range(rows):
    print(days[i])
    print(todo_list[i])
    print()

