def test_range(num, lower, upper):
    if not lower <= num <= upper:
        print(f"Число {num} не попадает в диапазон между {lower} и {upper}")
