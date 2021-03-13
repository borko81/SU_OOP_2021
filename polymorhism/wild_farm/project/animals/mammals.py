from project.animals.animal import Mammal
from project.food import Meat, Vegetable, Seed, Fruit


class Mouse(Mammal):
    def make_sound(self):
        return "Squeak"

    def feed(self, food):
        if isinstance(food, Vegetable) or isinstance(food, Fruit):
            self.weight += 0.10 * food.quantity
            self.food_eaten += food.quantity
            return
        return f'{self.__class__.__name__} does not eat {food.__class__.__name__}!'

    def __init__(self, name, weight, living_region):
        Mammal.__init__(self, name, weight, living_region)


class Dog(Mammal):
    def make_sound(self):
        return "Woof!"

    def feed(self, food):
        if isinstance(food, Meat):
            self.weight += 0.40 * food.quantity
            self.food_eaten += food.quantity
            return
        return f'{self.__class__.__name__} does not eat {food.__class__.__name__}!'

    def __init__(self, name, weight, living_region):
        Mammal.__init__(self, name, weight, living_region)


class Cat(Mammal):
    def make_sound(self):
        return "Meow"

    def feed(self, food):
        if isinstance(food, Meat) or isinstance(food, Vegetable):
            self.weight += 0.30 * food.quantity
            self.food_eaten += food.quantity
            return
        return f'{self.__class__.__name__} does not eat {food.__class__.__name__}!'

    def __init__(self, name, weight, living_region):
        Mammal.__init__(self, name, weight, living_region)


class Tiger(Mammal):
    def make_sound(self):
        return "ROAR!!!"

    def feed(self, food):
        if isinstance(food, Meat):
            self.weight += 1.00 * food.quantity
            self.food_eaten += food.quantity
            return
        return f'{self.__class__.__name__} does not eat {food.__class__.__name__}!'

    def __init__(self, name, weight, living_region):
        Mammal.__init__(self, name, weight, living_region)
