import random

#Сортировка выбором

"""
1) Находим наименьший элемент в массиве.
2) Обмениваем его с элементом на первой позиции.
3) Повторяем это для подмассива, начиная со второго элемента, и ищем наименьший элемент.
4) Обмениваем его с элементом на второй позиции.
5) Продолжаем так до тех пор, пока весь массив не будет отсортирован.
"""

def selection_sort(arr):
    n = len(arr)  # Определение длины массива
    for i in range(n - 1):  # Перебор всех элементов массива, кроме последнего
        min_index = i  # Предполагаем, что первый неотсортированный элемент является минимальным
        for j in range(i + 1, n):  # Перебор элементов, следующих за текущим i, для поиска наименьшего
            if arr[j] < arr[min_index]:  # Если найден элемент меньше, чем предполагаемый минимальный, то:
                min_index = j  # Обновляем индекс минимального элемента
        arr[i], arr[min_index] = arr[min_index], arr[i]  # Меняем местами текущий элемента с наименьшим найденным
    return arr

not_sorted = [random.randint(1, 50) for _ in range(10)]
print(not_sorted)
# [10, 37, 21, 50, 33, 47, 10, 50, 43, 25]

after_quick = selection_sort(not_sorted)
print(after_quick)
# [10, 10, 21, 25, 33, 37, 43, 47, 50, 50]
