import random


def retry_if_result_is_none(times=1):
    def decorator(func):
        def wrapper():
            for _ in range(times):
                result = func()
                if result:
                    return result
            return None
        return wrapper

    return decorator


@retry_if_result_is_none(times=2)
def test_function():
    return random.choice([None, "Passed"])


# Получилось получить значение за 2 вызова
print(test_function())
# Passed

# Не получилось получить значение за 2 вызова
print(test_function())
# None
