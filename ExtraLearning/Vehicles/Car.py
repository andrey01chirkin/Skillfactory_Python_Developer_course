from Transport import Transport


class Car(Transport):
    def __init__(self, mark, number, speed, load_capacity):
        super().__init__(mark, number, speed, load_capacity)

