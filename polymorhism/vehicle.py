from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_consumption = fuel_consumption
        self.fuel_quantity = fuel_quantity

    def drive(self, distance):
        result = (self.fuel_consumption + 0.9) * distance
        if result < self.fuel_quantity:
            self.fuel_quantity -= result

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    air = 1.6

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_consumption = fuel_consumption
        self.fuel_quantity = fuel_quantity

    def drive(self, distance):
        check_fuel_for_distance = (self.fuel_consumption + self.__class__.air) * distance
        if check_fuel_for_distance <= self.fuel_quantity:
            self.fuel_quantity -= check_fuel_for_distance

    def refuel(self, fuel):
        fuel *= 0.95
        self.fuel_quantity += fuel


if __name__ == '__main__':
    car = Car(20, 5)
    car.drive(3)
    print(car.fuel_quantity)
    car.refuel(10)
    print(car.fuel_quantity)

    truck = Truck(100, 15)
    truck.drive(5)
    print(truck.fuel_quantity)
    truck.refuel(50)
    print(truck.fuel_quantity)

