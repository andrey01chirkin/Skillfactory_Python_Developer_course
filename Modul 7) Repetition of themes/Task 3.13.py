from pprint import pprint

#При помощи генератора списков создайте таблицу умножения чисел от 1 до 10.

pprint([[i*j for j in range(1,11)] for i in range(1, 11)])

