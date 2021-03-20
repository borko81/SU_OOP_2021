from project.hardware.hardware import Hardware


class HeavyHardware(Hardware):
    def __init__(self, name: str, capacity: int, memory: int):
        super().__init__(name, 'Heavy', capacity=capacity * 2, memory=memory * 0.75)


if __name__ == '__main__':
    t = HeavyHardware('test',  100, 100)
    print(t.software_components)
