
'''
Вы участвуете в разработке онлайн-магазина. Вам необходимо реализовать класс Queue (очередь), чтобы
обрабатывать заказы в порядке их поступления.
Инициализатор этого класса должен создавать атрибут items — пустой список.

Реализуйте в классе методы:
- enqueue() — принимает один аргумент (идентификатор заказа) и добавляет его в конец списка items.
- is_empty() — возвращает True, если очередь пуста, и False — в противном случае.
- dequeue() — удаляет первый элемент списка items и возвращает его.
- show_queue() — выводит элементы списка items на экран в одну строку через пробел.

Пример работы класса:

# Создаём объект класса Queue
q = Queue()

# Добавляем элементы в очередь
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

# Выводим элементы очереди
q.show_queue()

# 1 2 3

# Удаляем элементы из очереди
q.dequeue()
q.dequeue()

# Выводим элементы очереди
q.show_queue()

# 3
'''

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, id):
        self.items.append(id)

    def is_empty(self):
        return len(self.items) == 0

    def dequeue(self):
        return self.items.pop(0)

    def show_queue(self):
        for item in self.items:
            print(item, end=' ')
        print()

# Создаём объект класса Queue
q = Queue()

# Добавляем элементы в очередь
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

# Выводим элементы очереди
q.show_queue()

# 1 2 3

# Удаляем элементы из очереди
q.dequeue()
q.dequeue()

# Выводим элементы очереди
q.show_queue()

# 3