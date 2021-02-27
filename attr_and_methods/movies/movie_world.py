from attr_and_methods.movies.customer import Customer
from attr_and_methods.movies.dvd import DVD


class MovieWorld:

    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer: Customer):
        if len(self.customers) < MovieWorld.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < MovieWorld.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd: int):
        user = [c for c in self.customers if c.id == customer_id][0]
        userdvd = [d for d in self.dvds if d.id == dvd][0]
        if userdvd in user.rented_dvds:
            return f"{user.name} has already rented {userdvd.name}"

        if userdvd.is_rented:
            return "DVD is already rented"

        if user.age < userdvd.age_restriction:
            return f"{user.name} should be at least {userdvd.age_restriction} to rent this movie"

        user.rented_dvds.append(userdvd)
        userdvd.is_rented = True
        return f"{user.name} has successfully rented {userdvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        user = [c for c in self.customers if c.id == customer_id][0]
        userdvd = [d for d in self.dvds if d.id == dvd_id][0]

        if not userdvd in user.rented_dvds:
            return f"{user.name} does not have that DVD"

        user.rented_dvds.remove(userdvd)
        userdvd.is_rented = False
        return f"{user.name} has successfully returned {userdvd.name}"

    def __repr__(self):
        return '\n'.join([repr(x) for x in (self.customers + self.dvds)])
