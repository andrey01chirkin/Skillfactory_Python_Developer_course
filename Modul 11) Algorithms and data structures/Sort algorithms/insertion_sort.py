#Сортировка вставками

"""
1) Начните со второго элемента массива (первый элемент считается уже отсортированным).
2) Сравните текущий элемент с предыдущими элементами, пока не найдете элемент, который меньше текущего.
3) Вставьте текущий элемент на свое место, сдвинув все элементы, которые больше него, на одну позицию вправо.
4) Повторите шаги 2 и 3 для всех оставшихся элементов.
"""

def insertion_sort(array):
  n = len(array)
  for i in range(1, n):
    key = array[i]
    j = i - 1
    while j >= 0 and key < array[j]:
      array[j + 1] = array[j]
      j -= 1
    array[j + 1] = key
  return array

import random

not_sorted = [random.randint(1, 50) for _ in range(10)]
print(not_sorted)
# [11, 18, 39, 5, 28, 20, 32, 5, 40, 34]

after_insertion = insertion_sort(not_sorted)
print(after_insertion)
# [5, 5, 11, 18, 20, 28, 32, 34, 39, 40
