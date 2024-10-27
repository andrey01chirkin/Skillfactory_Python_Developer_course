import os
from contextlib import contextmanager
from datetime import datetime
import time

class Timer:
    def __init__(self):
        pass

    def __enter__(self):
        self.start = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Time pass: {time.time() - self.start}")


@contextmanager #оборачиваем функцию в декоратор contextmanager
def timer():
    start = time.time()
    yield #если вам нужно что-то вернуть через контекстный менеджер, просто вставьте этот объект сюда.
    print(f"Time passed: {time.time() - start}")

with Timer():
    time.sleep(2)

with timer():
    time.sleep(1)

print(os.getcwd())





