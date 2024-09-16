def check_password(password):

    amount_digits = 0
    amount_uppers = 0
    amount_lowers = 0

    for item in password:
        if item.isdigit():
            amount_digits += 1
        if item.isupper():
            amount_uppers += 1
        if item.islower():
            amount_lowers += 1

    if len(password) < 8:
        print("Пароль должен быть не менее 8 символов")
    if not amount_uppers:
        print("Пароль должен содержать хотя бы одну заглавную букву")
    if not amount_lowers:
        print("Пароль должен содержать хотя бы одну строчную букву")
    if not amount_digits:
        print("Пароль должен содержать хотя бы одну цифру")

check_password("password")