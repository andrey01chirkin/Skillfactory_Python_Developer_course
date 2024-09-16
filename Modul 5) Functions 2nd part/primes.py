def primes(source_number):
    number = 0
    while number <= source_number:
        if number == 2 or number == 3 or number == 5:
            yield number
            number += 1
            continue
        if number % 2 != 0 and number % 3 != 0 and number % 5 != 0 and number != 1:
            yield number
            number += 1
            continue
        number += 1


prime_generator = primes(7)
for prime in prime_generator:
    print(prime)

# 2
# 3
# 5
# 7

