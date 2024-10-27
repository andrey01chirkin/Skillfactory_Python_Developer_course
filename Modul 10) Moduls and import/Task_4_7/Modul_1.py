
PI = 3.14

def circle_area(r: int):
    return PI*r**2

def rect_area(a: int, b: int):
    return a * b

if __name__ == "__main__":
    assert circle_area(5) == 78.5  # если ответы будут отличаться, то будет вызвана ошибка
    assert rect_area(5, 4) == 20