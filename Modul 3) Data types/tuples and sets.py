#Создайте кортеж family, в котором записаны имена членов вашей семьи,
# выведите нулевой и последний элемент кортежа, выведите каждый второй
# элемент кортежа, выведите длину вашего кортежа.
#Создайте множество цифр от 0 до 9. Напишите программу, которая принимает
# на вход целое число. Если это число есть в созданном множестве — программа
# удаляет число из множества, если числа нет в множестве — добавляет его в множество.
# После этого выводиться длина полученного множества и само множество.


family = ("Sveta", "Slava", "Tonya", "Liza", "Natasha")
print(family[0])
print(family[-1])
print(family[1::2])
print(len(family))

numbers_set = set()
for i in range(10):
    numbers_set.add(i)

number = int(input("Enter number for check: "))
if number in numbers_set:
    print('Удаляем число из множества')
    numbers_set.remove(number)
else:
    print('Добавляем число в множество')
    numbers_set.add(number)

print("Length: ", len(numbers_set))
print("Changed set: ", numbers_set)





