from project.appliances.tv import TV
from project.rooms.room import Room


class AloneYoung(Room):
    room_cost = 10

    def __init__(self, family_name: str, salary):
        super().__init__(family_name, budget=salary, members_count=1)
        self.appliances = [TV()]
        self.calculate_expenses(self.appliances)
