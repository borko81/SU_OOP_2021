from project.software.software import Software


class LightSoftware(Software):

    def __init__(self, name: str, capacity_consumption: int, memory_consumption: int):
        super().__init__(name, 'Light', capacity_consumption=capacity_consumption * 1.5, memory_consumption=memory_consumption - memory_consumption * 0.5)


if __name__ == '__main__':
    t = LightSoftware('test', 100, 100)
    print(t.capacity_consumption)
