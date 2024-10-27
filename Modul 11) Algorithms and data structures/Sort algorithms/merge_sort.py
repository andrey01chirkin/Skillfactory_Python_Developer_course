#Сортировка слиянием
"""
1) Разделите массив на две половины.
2) Рекурсивно отсортируйте каждую половину.
3) Слейте две отсортированные половины в один отсортированный массив.
"""
import random

def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

# left = sorted([random.randint(1, 50) for _ in range(5)])
# print('Left: ', left)
# right = sorted([random.randint(1, 50) for _ in range(5)])
# print('Right: ', right)
#
# after_merge = merge(left, right)
# print('After merge: ', after_merge)
# Left:  [9, 10, 16, 18, 36]
# Right:  [3, 20, 20, 21, 49]
# After merge:  [3, 9, 10, 16, 18, 20, 20, 21, 36, 49]

def merge_sort(array):
    if len(array) <= 1:
        return array
    # Разделяем массив на две половины
    middle = len(array) // 2
    left = merge_sort(array[:middle])
    right = merge_sort(array[middle:])
    # Сливаем отсортированные половины
    return merge(left, right)



arr = [random.randint(1, 50) for _ in range(10)]
print('Before merge_sort: ', arr)

sorted_arr = merge_sort(arr)
print('After merge_sort: ', sorted_arr)

# Before merge_sort:  [48, 35, 48, 15, 36, 7, 37, 44, 43, 39]
# After merge_sort:  [7, 15, 35, 36, 37, 39, 43, 44, 48, 48]