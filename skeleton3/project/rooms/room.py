class Room:
    room_cost = 0

    def __init__(self, family_name: str, budget: float, members_count: int):
        self.family_name = family_name
        self.budget = budget
        self.members_count = members_count
        self.children = []
        self.appliances = []
        self.expenses = 0

    @property
    def expenses(self):
        return self._expenses

    @expenses.setter
    def expenses(self, value):
        if value < 0:
            raise ValueError("Expenses cannot be negative")
        self._expenses = value

    def calculate_expenses(self, *args):
        cost = 0
        for i in args:
            for a in i:
                cost += a.cost * 30
        self.expenses = cost
        return self.expenses

    def total_room_expenses(self):
        return self.calculate_expenses(self.children, self.appliances) + self.room_cost
