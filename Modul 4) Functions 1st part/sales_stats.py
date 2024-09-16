
def sales_stats(sales_data, **kwargs):
    revenue = sum([sale[1]*sale[2] for sale in sales_data]) if kwargs.get('revenue') else None
    quantity = {}
    if kwargs.get('quantity'):
        for sale in sales_data:
            if sale[0] in quantity:
                quantity[sale[0]] += sale[1]
            else:
                quantity[sale[0]] = sale[1]
    else:
        quantity = None

    return revenue, quantity


sales_data = [["яблоки", 10, 20], ["груши", 5, 30], ["яблоки", 7, 20]]
print(sales_stats(sales_data, revenue=True))
# (490, None)
print(sales_stats(sales_data, quantity=True))
# (None, {'яблоки': 17, 'груши': 5})


