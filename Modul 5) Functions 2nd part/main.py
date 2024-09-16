import time
def decorator(func):
    def wrapper(*args, **kwargs):
        print("Hello1")
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print("Hello2")
        return round(end-start, 2)

    return wrapper


@decorator
def func(par1, par2):
    time.sleep(1.5)


print(func("Hello", " World"))
