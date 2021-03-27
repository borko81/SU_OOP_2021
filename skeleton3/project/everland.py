from project.rooms.room import Room


class Everland:

    def __init__(self):
        self.rooms = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        total_consumption = sum([r.room_cost for r in self.rooms])
        for r in self.rooms:
            total_consumption += sum([a.get_monthly_expense() for a in r.appliances])
            total_consumption += sum([c.cost for c in r.children]) * 30
        result = f"Monthly consumptions: {total_consumption:.2f}$."
        return result

    def pay(self):
        result = ''
        for r in self.rooms:
            ex = r.room_cost + r.calculate_expenses(r.appliances) * 30 + sum([c.cost for c in r.children]) * 30
            if r.budget >= ex:
                result += f"{r.family_name} paid {ex:.2f}$ and have {r.budget:.2f}$ left.\n"
                r.budget -= ex
            else:
                result += f"{r.family_name} does not have enough budget and must leave the hotel.\n"
                self.rooms.remove(r)
        return result

    def status(self):
        result = f"Total population: {sum([i.members_count for i in self.rooms])}\n"
        for r in self.rooms:
            result += f"{r.family_name} with {r.members_count} members. Budget: {r.budget:.2f}$, Expenses: {r.calculate_expenses(r.appliances) * 30 + sum([c.cost for c in r.children]) * 30:.2f}$\n"
            for n, c in enumerate(r.children, start=1):
                result += f"--- Child {n} monthly cost: {c.cost * 30:.2f}$\n"
            result += f"--- Appliances monthly cost: {r.calculate_expenses(r.appliances) * 30:.2f}$\n"
        return result