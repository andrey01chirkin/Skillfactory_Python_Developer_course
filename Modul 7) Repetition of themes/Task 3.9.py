num = int(input("Введите число: "))

if isinstance(num, int) and 100 < num <= 999 and num % 2 == 0 and num % 3 == 0:
    print("Число удовлетворяет условиям")

if all([isinstance(num, int) ,
        100 < num <= 999,
        num % 2 == 0,
        num % 3 == 0]):
    print("Число удовлетворяет условиям")