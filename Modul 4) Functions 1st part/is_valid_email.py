def is_valid_email(email):
    index_item = email.find("@")
    if index_item != -1 and not " " in email and "." in email[index_item + 1:]:
        return True
    else:
        return False


is_valid_email("user@example.com")
