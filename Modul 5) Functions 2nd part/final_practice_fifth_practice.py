categories = {
    "Электроника": {
        "Телефоны": {
            "Смартфоны": {},
            "Проводные": {}
        },
        "Компьютеры": {
            "Ноутбуки": {},
            "Стационарные": {
                "Игровые": {},
                "Для работы": {}
            }
        }
    },
    "Одежда": {
        "Мужская": {
            "Джинсы": {},
            "Куртки": {}
        }
    }
}

# def extract_categories(category_dict, parent_path=''):
#     paths = []
#     for key, value in category_dict.items():
#         current_path = f"{parent_path} > {key}" if parent_path else key
#         paths.append(current_path)
#         paths.extend(extract_categories(value, current_path))
#     return paths


def extract_categories(category_dict, parent_path=''):
    paths = []
    for key, value in category_dict.items():
        path = f"{parent_path} > {key}" if parent_path else key
        paths.append(path)
        paths += extract_categories(value, path)
    return paths

def factorial(n):
    if n == 0:
        return 1
    return n*factorial(n-1)

print(factorial(3))

def fibonacci(n):
    if n in (1,2):
        return 1
    return fibonacci(n-1)+fibonacci(n-2)

print(fibonacci(4))

def extract_categories(category_dict, parent_path=''):
    paths = []
    for category, categories in category_dict.items():
        path = f"{parent_path} > {category}" if parent_path else category
        paths.append(path)
        paths += extract_categories(categories, path)
    return paths

paths = extract_categories(categories, parent_path='root')
for path in paths:
    print(path)
# root > Электроника
# root > Электроника > Телефоны
# root > Электроника > Телефоны > Смартфоны
# root > Электроника > Телефоны > Проводные
# root > Электроника > Компьютеры
# root > Электроника > Компьютеры > Ноутбуки
# root > Электроника > Компьютеры > Стационарные
# root > Электроника > Компьютеры > Стационарные > Игровые
# root > Электроника > Компьютеры > Стационарные > Для работы
# root > Одежда
# root > Одежда > Мужская
# root > Одежда > Мужская > Джинсы
# root > Одежда > Мужская > Куртки

paths = extract_categories(categories)
for path in paths:
    print(path)

# Электроника
# Электроника > Телефоны
# Электроника > Телефоны > Смартфоны
# ...
# Одежда > Мужская
# Одежда > Мужская > Джинсы
# Одежда > Мужская > Куртки
