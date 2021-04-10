from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class Controller:
    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        if aquarium_type == 'FreshwaterAquarium':
            self.aquariums.append(FreshwaterAquarium(aquarium_name))
            return f"Successfully added {aquarium_type}."
        elif aquarium_type == "SaltwaterAquarium":
            self.aquariums.append(SaltwaterAquarium(aquarium_name))
            return f"Successfully added {aquarium_type}."
        else:
            return "Invalid aquarium type."

    def add_decoration(self, decoration_type: str):
        if decoration_type == 'Ornament':
            self.decorations_repository.add(Ornament())
            return f"Successfully added {decoration_type}."
        elif decoration_type == 'Plant':
            self.decorations_repository.add(Plant())
            return f"Successfully added {decoration_type}."
        else:
            return "Invalid decoration type."

    def insert_decoration(self, aquarium_name: str, decoration_type: str):

        try:
            temp_a = [a for a in self.aquariums if a.name == aquarium_name][0]
            temp_d = [d for d in self.decorations_repository.decorations if
                      d.__class__.__name__ == decoration_type][0]
            temp_a.add_decoration(temp_d)
            self.decorations_repository.remove(temp_d)
            return f"Successfully added {decoration_type} to {aquarium_name}."
        except IndexError:
            return f"There isn't a decoration of type {decoration_type}."

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        if fish_type not in ["FreshwaterFish", "SaltwaterFish"]:
            return f"There isn't a fish of type {fish_type}."
        try:
            temp_a = [a for a in self.aquariums if a.name == aquarium_name][0]

            if fish_type == "FreshwaterFish" and temp_a.__class__.__name__ == 'FreshwaterAquarium':
                return temp_a.add_fish(FreshwaterFish(fish_name, fish_species, price))
            elif fish_type == "SaltwaterFish" and temp_a.__class__.__name__ == 'SaltwaterAquarium':
                return temp_a.add_fish(SaltwaterFish(fish_name, fish_species, price))
            else:
                return "Water not suitable."
        except IndexError:
            pass

    def feed_fish(self, aquarium_name: str):
        fed_count = 0
        for a in self.aquariums:
            if a.name == aquarium_name:
                for fishs in a.fish:
                    fishs.eat()
                    fed_count += 1
        return f"Fish fed: {fed_count}"

    def calculate_value(self, aquarium_name: str):
        value = 0
        temp_a = [a for a in self.aquariums if a.name == aquarium_name][0]
        value += sum([f.price for f in temp_a.fish])
        value += sum([d.price for d in temp_a.decorations])
        return f"The value of Aquarium {aquarium_name} is {value:.2f}."

    def report(self):
        result = ''
        for a in self.aquariums:
            result += a.__str__()
        return result
