def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a+b


fibonacci_generator = fibonacci(7)
for number in fibonacci_generator:
    print(number)
# 0
# 1
# 1
# 2
# 3
# 5
# 8
