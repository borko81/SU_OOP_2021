class Vehicle:
    color = 'white'

    def __init__(self, max_speed, mileage, price):
        self.max_speed = max_speed
        self.mileage = mileage
        self.price = price

    def seating_capacity(self, capacity):
        return "The seating capacity is %d" % capacity

    def fare(self):
        return self.price * 100


class Bus(Vehicle):
    def __init__(self, max_speed, mileage, price):
        # Vehicle.__init__(self, max_speed, mileage)
        super().__init__(max_speed, mileage, price)

    def seating_capacity(self, capacity: int = 50):
        """Use default parameter, return super method"""
        return super().seating_capacity(capacity)

    def fare(self):
        amount = super().fare()
        return amount * 10


if __name__ == "__main__":
    modelX = Bus(240, 18, 10)
    print(modelX.max_speed, modelX.mileage)
    print(modelX.seating_capacity())
    print(modelX.color)
    print(modelX.fare())
    print(type(modelX))
    print(isinstance(modelX, Vehicle))
