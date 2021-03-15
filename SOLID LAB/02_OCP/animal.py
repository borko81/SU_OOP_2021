from abc import ABC, abstractmethod


class SomeAnimal(ABC):
    @abstractmethod
    def __repr__(self):
        pass


class Cat(SomeAnimal):
    def __repr__(self):
        return "meow"


class Dog(SomeAnimal):
    def __repr__(self):
        return "wolf-wolf"


class Animal:
    def __init__(self, species):
        self.species = species

    def get_species(self):
        return self.species


def animal_sound(animals: list):
    for animal in animals:
        print(animal.get_species())


animals = [Animal(Cat()), Animal(Dog())]
animal_sound(animals)

