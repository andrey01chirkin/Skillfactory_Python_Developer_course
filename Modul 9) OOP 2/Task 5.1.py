class TaskList:
    def __init__(self):
        self.__task_list = []

    def __is_task_in_list(self, task):
        return any(filter(lambda task_: task_['name'] == task, self.__task_list))

    def add_task(self, task):
        if self.__is_task_in_list(task):
            print(f"Задача \"{task}\" уже есть в списке")
        else:
            self.__task_list.append({'name': task, 'done': False})
            print(f"Задача \"{task}\" добавлена в список")

    def remove_task(self, task_name):
        if self.__is_task_in_list(task_name):
            self.__task_list = list(filter(lambda task_: task_['name'] != task_name, self.__task_list))
            print(f"Задача \"{task_name}\" удалена из списка")
        else:
            print(f"Задачи \"{task_name}\" нет в списке")


# Создаём контейнер задач
ts = TaskList()
# Добавляем задачи в контейнер
ts.add_task('Create get_task_list() method')

# Пытаемся добавить две одинаковые задач
ts.add_task('Show students how __task_list attr looks like')
ts.add_task('Show students how __task_list attr looks like')

# Добавляем задачу и удаляем ее
ts.add_task('Show students how work remove_task() method')
ts.remove_task('Show students how work remove_task() method')

# Смотрим приватный список задач
print(ts._TaskList__task_list)

# Задача "Create get_task_list() method" добавлена в список
# Задача "Show students how __task_list attr looks like" добавлена в список
# Задача "Show students how __task_list attr looks like" уже есть в списке
# Задача "Show students how work remove_task() method" добавлена в список
# Задача "Show students how work remove_task() method" удалена из списка
# [{'name': 'Create get_task_list method', 'done': False}, {'name': 'Show students how __task_list attr looks like', 'done': False}]
