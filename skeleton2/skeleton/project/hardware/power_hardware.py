from project.hardware.hardware import Hardware


class PowerHardware(Hardware):
    def __init__(self, name: str, capacity: int, memory: int):
        super().__init__(name, 'Power', capacity=capacity * 0.25, memory=memory + memory * 0.75)


if __name__ == '__main__':
    t = PowerHardware('test', 100, 100)
    print(t.software_components)