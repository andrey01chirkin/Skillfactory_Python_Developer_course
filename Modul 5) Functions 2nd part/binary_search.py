def binary_search(lst, num):
    left = 0
    right = len(lst)
    index_middle_item = len(lst)//2
    middle_item = lst[index_middle_item]
    if middle_item == num:
        return True
    if num < middle_item:
        right = index_middle_item
        return binary_search(lst[left:right], num)
    if num > middle_item:
        left = index_middle_item+1
        if left >= right:
            return False
        return binary_search(lst[left:right], num)


print(binary_search([1, 2, 3, 4, 5], 4))
# True
print(binary_search([1, 2, 3, 4, 5], 6))
# False
