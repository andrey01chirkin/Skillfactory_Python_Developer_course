class SellItem:
    def __init__(self, name: str, price: int | float):
        self.name = name
        self.price = price


# ваш код здесь
class House(SellItem):
    def __init__(self, name: str, price: int | float, material: str, square: int | float):
        super().__init__(name, price)
        self.material = material
        self.square = square


# ваш код здесь
class Flat(SellItem):
    def __init__(self, name: str, price: int | float, size: int | float, rooms: int | float):
        super().__init__(name, price)
        self.size = size
        self.rooms = rooms


# ваш код здесь
class Agency:
    def __init__(self, name: str):
        self.name = name
        self.objs = []

    def add_object(self, obj: object):
        self.objs.append(obj)

    def remove_obj(self, obj: object):
        if obj in self.objs:
            self.objs.remove(obj)

    def get_objects(self):
        return self.objs


# Создаём агентство недвижимости
real_estate_agency = Agency("Best Homes Agency")

# Создаём объекты недвижимости
house1 = House(name="Уютный дом", price=200000, material="Кирпич", square=150)
flat1 = Flat(name="Современная квартира", price=100000, size=80, rooms=2)

# Добавляем объекты недвижимости в агентство
real_estate_agency.add_object(house1)
real_estate_agency.add_object(flat1)

# Получаем список доступных объектов недвижимости
properties = real_estate_agency.get_objects()

for p in properties:
    print(type(p), p.__dict__)

# <class '__main__.House'> {'name': 'Уютный дом', 'price': 200000, 'material': 'Кирпич', 'square': 150}
# <class '__main__.Flat'> {'name': 'Современная квартира', 'price': 100000, 'size': 80, 'rooms': 2}

print(SellItem(name = 'Item 1', price = 100).name)
print(SellItem(name = 'Item 1', price = 100).price)
print(House(name = 'Item 1', price = 100, material = 'Brick', square = 150).material)