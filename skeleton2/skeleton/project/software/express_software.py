from project.software.software import Software


class ExpressSoftware(Software):

    def __init__(self, name: str, capacity_consumption: int, memory_consumption: int):
        super().__init__(name, 'Express', capacity_consumption, memory_consumption=memory_consumption * 2)


if __name__ == '__main__':
    t = ExpressSoftware('test', 100, 100)
    print(t.capacity_consumption)