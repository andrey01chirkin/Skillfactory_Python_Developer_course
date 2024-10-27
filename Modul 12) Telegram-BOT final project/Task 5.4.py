import json

import redis

red = redis.Redis(
    host="redis-15469.c326.us-east-1-3.ec2.redns.redis-cloud.com",
    port=15469,
    password="Og6fHlTuj2AQvpgtQ6isNh4y0kBf1bMA"
)

class Friends:
    def __init__(self):
        pass

    def add_phone(self, name, phone):
        red.set(name, json.dumps(phone))

    def show_phone(self, name):
        phone_ = red.get(name)
        if phone_:
            phone = json.loads(phone_)
            print(name, phone)

    def delete_phone(self, name):
        if red.get(name):
            red.delete(name)

f = Friends()
f.add_phone('Oleg', '+7(999)999-99-99')
f.add_phone('Stas', '+7(888)888-88-88')
f.add_phone('Semen', '+7(777)777-77-77')
f.show_phone('Oleg')
f.show_phone('Stas')
f.show_phone('Semen')
print()

f.delete_phone('Oleg')
f.delete_phone('Semen')

f.show_phone('Oleg')
f.show_phone('Stas')
f.show_phone('Semen')