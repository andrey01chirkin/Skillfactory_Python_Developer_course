
class RestaurantQueue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def add_order(self, order):
        self.queue.append(order)
        print(f"Заказ от {order.customer_name} добавлен в очередь.")

    def take_order(self):
        if not self.is_empty():
            order = self.queue.pop(0)
            order.status = "в процессе"
            print(f"Заказ от {order.customer_name} взят в работу.")
            return order
        else:
            print("Очередь заказов пуста.")
            return None

    def complete_order(self, order):
        order.status = "готов"
        print(f"Заказ от {order.customer_name} готов.")

    def print_queue(self):
        if self.is_empty():
            print("Очередь заказов пуста.")
        else:
            print("Текущие заказы:")
            for i, order in enumerate(self.queue):
                print(f"{i + 1}. Заказ от {order.customer_name} ({order.status})")
