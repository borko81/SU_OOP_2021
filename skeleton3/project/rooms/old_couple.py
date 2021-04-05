from project.appliances.fridge import Fridge
from project.appliances.stove import Stove
from project.appliances.tv import TV
from project.rooms.room import Room


class OldCouple(Room):
    room_cost = 15

    def __init__(self, family_name: str, pension_one, pension_two):
        super().__init__(family_name, budget=pension_one + pension_two, members_count=2)
        self.appliances = self.appliances = [TV() for _ in range(self.members_count)] + [Stove() for _ in range(self.members_count)] + [Fridge() for _ in range(self.members_count)]
        self.calculate_expenses(self.appliances)


if __name__ == '__main__':
    test = OldCouple('St', 100, 100)
    print(test.expenses)


