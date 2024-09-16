def is_success_code(code):
    if 200 <= code <= 299:
        return True
    else:
        return False