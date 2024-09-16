def create_counter():
    counter = 0

    def counter_func():
        nonlocal counter
        counter += 1
        return counter

    return counter_func


counter = create_counter()
print(counter())  # вернет "1"
print(counter())  # вернет "2"
print(counter())  # вернет "3"

# 1
# 2
# 3
