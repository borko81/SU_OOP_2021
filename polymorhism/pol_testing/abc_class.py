from abc import ABC, abstractmethod


class Abstract(ABC):
    PRICE = 0

    @abstractmethod
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def show_name_capitalize(self):
        return self.name.title()

    @abstractmethod
    def show_price(self):
        return self.__class__.PRICE