def binary_search(lst, num):
    if len(lst) == 0:
        return False
    else:
        midpoint = len(lst) // 2
        if lst[midpoint] == num:
            return True
        else:
            if num < lst[midpoint]:
                return binary_search(lst[:midpoint], num)
            else:
                return binary_search(lst[midpoint+1:], num)


print(binary_search([1, 2, 3, 4, 5], 4))
# True
print(binary_search([1, 2, 3, 4, 5], 6))
# False