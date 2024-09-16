def sort_data(**kwargs):
    return sorted(kwargs.items())


print(sort_data(name='Alex', age=30, city='New York'))
# [('age', 30), ('city', 'New York'), ('name', 'Alex')]