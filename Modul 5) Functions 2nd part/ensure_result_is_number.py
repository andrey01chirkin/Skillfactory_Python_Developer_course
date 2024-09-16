import random


def ensure_result_is_number(func):
    def wrapper():
        result = func()
        return result if isinstance(result, int | float) else None

    return wrapper


@ensure_result_is_number
def test_function():
    return random.choice(["Passed", 10, "Failed", 5.5])


# Функция вернула не int и не float
print(test_function())
# None

# Функция вернула float
print(test_function())
# 5.5

# Функция вернула int
print(test_function())
# 10
