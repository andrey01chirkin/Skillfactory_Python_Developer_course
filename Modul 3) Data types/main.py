from random import randint
from pprint import pprint

data = []

rows = 10
columns = 5

for i in range(rows):
    tmp = []
    for j in range(columns):
        tmp.append(randint(0,100))
    data.append(tmp)

pprint(data)

for i in range(rows):
    for j in range(columns):
        if j == 2:
            data[i].pop(j)

pprint(data)