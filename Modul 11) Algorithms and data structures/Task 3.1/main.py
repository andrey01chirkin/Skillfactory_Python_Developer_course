from RestaurantQueue import RestaurantQueue
from Order import Order

if __name__ == "__main__":
    queue = RestaurantQueue()
    queue.add_order(Order(1, "Андрей", ["Суп картофельный", "Салат Цезарь с курицей", "Картошка с грибами"]))
    queue.add_order(Order(2, "Семен", ["Борщ", "Салат Цезарь с криветками", "Гречка с курицей"]))
    queue.add_order(Order(3, "Сергей", ["Солянка", "Салат овощной", "Стейк с картошкой"]))

    queue.print_queue()

    order_in_progress = queue.take_order()

    queue.print_queue()

    queue.complete_order(order_in_progress)

