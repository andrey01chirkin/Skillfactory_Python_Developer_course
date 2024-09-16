def sales_stats(sales_data, **kwargs):
    revenue = sum([sale[1] * sale[2] for sale in sales_data]) if kwargs.get('revenue') else None
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
print(sales_stats(sales_data, customers=True))
# (None, None)

print()


def create_report(sales_data, func):
    revenue, quantity = func(sales_data, quantity=True)
    result_string = ""
    if revenue:
        result_string += f"Средний доход за данный период составил {revenue / len(sales_data)}.\n"
    if quantity:
        result_string += f"Количество проданных единиц каждого товара:\n"
        for key in quantity:
            result_string += f"{key}: {quantity.get(key)}\n"

    return result_string


sales_data = [["яблоки", 20, 20], ["груши", 5, 30], ["яблоки", 7, 20]]
print(create_report(sales_data, sales_stats))
# Средний доход за данный период составил 230.0.
# Количество проданных единиц каждого товара:
# яблоки: 27
# груши: 5

def dummy_func(data, **kwargs):
    revenue = 100.0
    quantity = {"Apple": 10, "Orange": 5}
    return revenue, quantity
print(create_report([('Apple', 10, 0.5), ('Orange', 5, 0.6)], dummy_func))