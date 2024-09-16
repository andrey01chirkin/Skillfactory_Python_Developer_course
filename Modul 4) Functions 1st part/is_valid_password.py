
def is_valid_password(password, min_length=8, require_digit=True, require_upper=True, require_lower=True):

    has_digits = False
    has_uppers = False
    has_lowers = False

    if len(password) < min_length:
        return False

    for item in password:
        if require_digit and item.isdigit():
            has_digits = True
        if require_upper and item.isupper():
            has_uppers = True
        if require_lower and item.islower():
            has_lowers = True

    if require_digit and not has_digits:
        return False
    if require_upper and not has_uppers:
        return False
    if require_upper and not has_lowers:
        return False

    return True

print(is_valid_password('ABCdef', min_length=6, require_upper=True, require_lower=True, require_digit=False))