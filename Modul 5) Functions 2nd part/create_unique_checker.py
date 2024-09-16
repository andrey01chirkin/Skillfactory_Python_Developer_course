def create_unique_checker():
    data = set()

    def checker(value):
        if value in data:
            return False
        else:
            data.add(value)
            return True

    return checker


unique_checker = create_unique_checker()
print(unique_checker(5))
print(unique_checker(5))
print(unique_checker(10))

# True
# False
# True
