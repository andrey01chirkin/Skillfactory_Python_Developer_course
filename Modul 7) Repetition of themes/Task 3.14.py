from pprint import pprint

#Модифицируйте последний пример таким образом, чтобы в список сохранялось True,
# если элемент четный, и False, если элемент нечетный.

pprint([int(input()) % 2 == 0 for i in range(5)])

