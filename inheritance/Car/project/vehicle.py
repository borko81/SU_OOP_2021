from typing import ClassVar


class Vehicle:
    DEFAULT_FUEL_CONSUMPTION: ClassVar[float] = 1.25

    def __init__(self, fuel, horse_power) -> object:
        self.fuel = fuel
        self.horse_power = horse_power
        self.fuel_consumption = self.__class__.DEFAULT_FUEL_CONSUMPTION

    def drive(self, kilometers):
        temp = kilometers * self.fuel_consumption
        if temp <= self.fuel:
            self.fuel -= temp
