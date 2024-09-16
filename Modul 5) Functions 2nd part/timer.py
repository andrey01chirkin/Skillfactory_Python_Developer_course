import time

def timer():
    start = time.time()

    def elapsed():
        nonlocal start
        end = time.time()
        elapsed = end - start
        start = end
        return elapsed

    return elapsed



my_timer = timer()
print(int(my_timer()))  # int — для приближенного значения секунд
# Ждем немного...
time.sleep(2)
print(int(my_timer()))

time.sleep(1)
print(int(my_timer()))

# Вывод:
# 0
# 2

