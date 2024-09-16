import random


def generate_test_data(n=5, min_value=1, max_value=10):
    return [random.randint(min_value, max_value) for i in range(n)]


print(generate_test_data(15, 0, 10))


