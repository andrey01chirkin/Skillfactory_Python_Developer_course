# Программа должна уметь хранить записи телефонной книги в виде: имя:номер телефона, а также
# добавлять, удалять и редактировать записи и выводить телефонную книгу в удобном формате —
# каждая запись на отдельной строке.

# Создайте словарь — телефонную книгу номеров ваших друзей, где ключом является имя, а значением телефон.
# Выведите в консоль только имена ваших друзей (метод key ()), выведите в консоль только номера телефонов
# (метод value()).
# Используя цикл, выведите записи из вашей телефонной книге вида: Контакт: {Имя} Телефон: {Номер телефона}
# (метод items()).
# Добавьте с помощью консоли номера телефонов для двух новых друзей.
# Поменяйте номер телефона одного из ваших друзей на новый.
# Введите имя друга в консоли, если друг есть в вашей телефонной книжке — удалите запись, если
# нет — добавьте запись, считав номер телефона с консоли.

contacts = {}

while True:
    name = input("Введите имя: ")
    if name == "-1":
        break
    number = input("Введите номер телефона: ")
    contacts[name] = number

print()

print(contacts.keys())
print()

print(contacts.values())
print()

for name, value in contacts.items():
    print(f"Контакт: {name} Телефон: {value}")

print()

print("Добавление новых контактов в телефонную книгу")
for i in range(2):
    name = input("Введите имя контакта: ")
    phone = input(f"Введите номер для {name}: ")
    contacts[name] = phone

print(contacts)
print()

print("Замена номера телефона")
name = input("Введите имя контакта: ")
number = input(f"Введите новый номер {name}: ")
if name in contacts.keys():
    contacts[name] = number
    print("Номер изменен")
else:
    print("Контакт не найден в телефонной книге")

print(contacts)
print()

print("Удаление или добавление номера из телефонной книги")
name = input("Введите имя из телефонной книги:")
if name in contacts.keys():
    del contacts[name]
    print("Контакт удален")
else:
    number = input("Введите имя из телефонной книги: ")
    contacts[name] = number

print(contacts)


