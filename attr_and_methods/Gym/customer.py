class Customer:
    id = 0

    def __init__(self, name: str, address: str, email: str):
        self.name = name
        self.address = address
        self.email = email
        self.id = self.get_next_id()

    @staticmethod
    def get_next_id():
        Customer.id += 1
        return Customer.id

    def __repr__(self) -> str:
        return f"Customer <{self.id}> {self.name}; Address: {self.address}; Email: {self.email}"


if __name__ == '__main__':
    customer1 = Customer("John", "Maple Street", "john.smith@gmail.com")
    customer2 = Customer("John", "Maple Street", "john.smith@gmail.com")
    print(customer2.id)