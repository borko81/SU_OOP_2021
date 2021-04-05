from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.rooms.room import Room


class YoungCouple(Room):
    room_cost = 20

    def __init__(self, family_name: str, salary_one, salary_two):
        super().__init__(family_name, budget=salary_one + salary_two, members_count=2)
        self.appliances = [TV() for _ in range(self.members_count)] + [Fridge() for _ in range(self.members_count)] + [Laptop() for _ in range(self.members_count)]
        self.calculate_expenses(self.appliances)

