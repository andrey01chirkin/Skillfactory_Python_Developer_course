
#Напишите рекурсивную функцию, находящую минимальный элемент списка без использование циклов и встроенной функции min().

def min_list(L):
    if len(L) == 1:
        return L[0]
    return L[0] if L[0] < min_list(L[1:]) else min_list(L[1:])

print(min_list([15, 4, 19, 37, 5]))

