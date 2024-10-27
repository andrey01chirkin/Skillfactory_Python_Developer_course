
class Order:
    def __init__(self, order_id, customer_name, dishes, status="новый"):
        self.order_id = order_id
        self.customer_name = customer_name
        self.dishes = dishes
        self.status = status

