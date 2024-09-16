phone_numbers = ['123-456-7890', '123.456.7890', '(123) 456-7890', '+1234567890', '1234567890']


def format_phone_number(number):
    it = filter(lambda item: item.isdigit(), number)
    result_str = ""
    for item in it:
        result_str += item
    return result_str
    #return ''.join(filter(lambda item: item.isdigit(), number))


formatted_numbers = list(map(format_phone_number, phone_numbers))
print(formatted_numbers)
