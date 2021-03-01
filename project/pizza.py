class Pizza:

    def __init__(self, name, dough, toppings_capacity):
        self.__name = name
        self.__dough = dough
        self.__toppings = {}
        self.__toppings_capacity = toppings_capacity

    @property
    def name(self):
        return self.__name

    @name.setter
    def flour_type(self, value):
        self.__name = value

    @property
    def dough(self):
        return self.__dough

    @dough.setter
    def dough(self, value):
        self.__dough = value

    @property
    def toppings(self):
        return self.__toppings

    @toppings.setter
    def toppings(self, value):
        self.__toppings = value

    @property
    def toppings_capacity(self):
        return self.__toppings_capacity

    @toppings_capacity.setter
    def toppings_capacity(self, value):
        self.__toppings_capacity = value

    def add_topping(self, topping):
        if self.__toppings_capacity <= 0:
            raise ValueError("Not enough space for another topping")

        if topping.topping_type not in self.toppings:
            self.toppings[topping.topping_type] = topping.weight

        else:
            self.toppings[topping.topping_type] += topping.weight

    def calculate_total_weight(self):
        total = 0
        for _, value in self.__toppings.items():
            total += value
        return total
