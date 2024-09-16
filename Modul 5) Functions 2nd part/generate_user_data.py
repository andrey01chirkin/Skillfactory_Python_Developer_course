import random


def generate_user_data(size, first_names, last_names, rng):
    for i in range(size):
        name = random.choice(first_names)
        surname = random.choice(last_names)
        age = random.randint(rng[0], rng[1])
        yield name, surname, age


first_names = ["Alice", "Bob", "Charlie"]
last_names = ["Smith", "Johnson", "Williams"]
user_data_generator = generate_user_data(5, first_names, last_names, [18, 60])
for user in user_data_generator:
    print(user)

print(list(generate_user_data(5, ["Alice", "Bob", "Charlie"], ["Smith", "Johnson", "Williams"], (20, 40))))
# ('Charlie', 'Williams', 19)
# ('Charlie', 'Johnson', 48)
# ('Bob', 'Johnson', 26)
# ('Charlie', 'Smith', 36)
# ('Charlie', 'Johnson', 35)

