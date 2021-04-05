from project.rooms.room import Room


class Everland:

    def __init__(self):
        self.rooms = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        total_consumption = 0
        for r in self.rooms:
            total_consumption += r.total_room_expenses()
        result = f"Monthly consumtions: {total_consumption:.2f}$."
        return result

    def pay(self):
        result = ''
        for r in self.rooms:
            ex = r.total_room_expenses()
            if r.budget >= ex:
                r.budget -= ex
                result += f"{r.family_name} paid {ex:.2f}$ and have {r.budget:.2f}$ left.\n"
            else:
                self.rooms.remove(r)
                result += f"{r.family_name} does not have enough budget and must leave the hotel.\n"
        return result.strip()

    def status(self):
        result = f"Total population: {sum([i.members_count for i in self.rooms])}\n"
        for r in self.rooms:
            result += f"{r.family_name} with {r.members_count} members. Budget: {r.budget:.2f}$, Expenses: {r.expenses:.2f}$\n"
            for n, c in enumerate(r.children, start=1):
                result += f"--- Child {n} monthly cost: {c.get_monthly_expense():.2f}$\n"
            result += f"--- Appliances monthly cost: {sum(a.get_monthly_expense() for a in r.appliances):.2f}$\n"
        return result
