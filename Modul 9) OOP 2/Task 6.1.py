class Model:
    def __init__(self):
        self.__name = None

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if 3 <= len(name) <= 15:
            self.__name = name


# Создаем экземпляр класса Model
m = Model()

# Проверяем начальное значение имени модели (должно быть None)
print(m.name)
# Выведет: None

# Пытаемся установить значение имени, которое не соответствует условиям
m.name = "AB"
print(m.name)
# Выведет: None

# Пытаемся установить значение имени, которое не соответствует условиям
m.name = "A" * 16
print(m.name)
# Выведет: None

# Устанавливаем корректное значение имени
m.name = "ValidModelName"
print(m.name)
# Выведет: ValidModelName
