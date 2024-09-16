def square(n):
    return n ** 2


def test_function(arg, res):
    if square(arg) == res:
        return True
    else:
        return False


print(test_function( 4, 16))  # Передаем имя функции
print(test_function( 5, 20))
