
def sort_strings_by_last_char(strings):
    return sorted(strings,key=lambda string: string[-1])


strings = ["apple", "banana", "cherry", "date", "elderberry"]
print(sort_strings_by_last_char(strings))
# ['banana', 'apple', 'date', 'elderberry', 'cherry']


