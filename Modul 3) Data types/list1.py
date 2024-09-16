#1)Создайте массив coworkers, в котором записаны имена ваших коллег, выведите
# имя первого и последнего коллеги, выведите имена каждого первого и каждого
# второго коллеги, выведите количество ваших коллег.
#2) Считайте с консоли имя нового коллеги и добавьте его в массив. Выведите
# полученный список ваших коллег и его длину.
#3) Считайте с консоли имя человека, проверьте, работает ли он с вами, и
# выведите соответствующее сообщение.

coworkers = ["Oleg", "Andrew", "Stas", "Semen", "John"]

print(f"First item: {coworkers[0]}, \nLast item: {coworkers[-1]}")
print(coworkers[::2])
print(coworkers[1::2])
print(f"Amount of coworkers: ", len(coworkers))

name = input("Name new coworker: ")
coworkers.append(name)
print(coworkers)
print(len(coworkers))

new_coworker = input("Enter name to check: ")
if new_coworker in coworkers:
    print("There is this person")
else:
    print("There is not this person")








