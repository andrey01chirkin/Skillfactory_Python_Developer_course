#Быстрая сортировка

"""
1) Выберите элемент из массива в качестве опорного элемента (посередине).
2) Разделите массив на два подмассива:
    - левый подмассив содержит элементы, которые меньше опорного элемента;
    - правый подмассив содержит элементы, которые больше опорного элемента.
3) Рекурсивно отсортируйте левый и правый подмассивы.
4) Объедините отсортированные подмассивы и опорный элемент в отсортированный массив.
"""

def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array[len(array) // 2]

    left = [x for x in array if x < pivot]
    middle = [x for x in array if x == pivot]
    right = [x for x in array if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


import random

not_sorted = [random.randint(1, 50) for _ in range(10)]
print(not_sorted)
# [10, 37, 21, 50, 33, 47, 10, 50, 43, 25]

after_quick = quick_sort(not_sorted)
print(after_quick)
# [10, 10, 21, 25, 33, 37, 43, 47, 50, 50]