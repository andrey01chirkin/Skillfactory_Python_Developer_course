


try:
    num = int(input("Ввежите строку: "))
except ValueError:
    print("Вы ввели неправильное число")
else:
    print("Вы ввели правильное число")
finally:
    print("Выход из программы")



