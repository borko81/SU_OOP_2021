from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:

    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        power = PowerHardware(name, capacity, memory)
        System._hardware.append(power)

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        power = HeavyHardware(name, capacity, memory)
        System._hardware.append(power)

    @staticmethod
    def register_express_software(hardware_name: str, name:str, capacity_consumption:int, memory_consumption:int):
        try:
            temp = [name for name in System._hardware if name.name == hardware_name][0]
            e = ExpressSoftware(name, capacity_consumption, memory_consumption)
            try:
                temp.install(e)
                System._software.append(e)
            except Exception as e:
                return e
        except IndexError:
            return "Hardware does not exist"

    @staticmethod
    def register_light_software(hardware_name: str, name:str, capacity_consumption:int, memory_consumption:int):
        try:
            temp = [name for name in System._hardware if name.name == hardware_name][0]
            e = LightSoftware(name, capacity_consumption, memory_consumption)
            try:
                temp.install(e)
                System._software.append(e)
            except Exception as e:
                return e
        except IndexError:
            return "Hardware does not exist"

    @staticmethod
    def release_software_component(hardware_name:str, software_name:str):
        try:
            h = [name for name in System._hardware if name.name == hardware_name][0]
            s = [name for name in System._software if name.name == software_name][0]
        except IndexError:
            return "Some of the components do not exist"
        else:
            h.uninstall(s)

    @staticmethod
    def analyze():
        total_meomory = sum([m.memory for m in System._hardware])
        total_used_memory = sum([m.memory_consumption for m in System._software])

        total_capacity = sum([m.capacity for m in System._hardware])
        total_used_space = sum([m.capacity_consumption for m in System._software])

        message = "System Analysis\n"
        message += f"Hardware Components: {len(System._hardware)}\n"
        message += f"Software Components: {len(System._software)}\n"
        message += f"Total Operational Memory: {int(total_used_memory)} / {int(total_meomory)}\n"
        message += f"Total Capacity Taken: {int(total_used_space)} / {int(total_capacity)}"
        return message

    @staticmethod
    def system_split():
        result = ''
        for h in System._hardware:
            result += h.__repr__()
        return result


if __name__ == '__main__':
    test = System()
    test.register_power_hardware('HDD', 50, 50)
    print(test.register_express_software('HDD', 'p', 100, 1000))
    # print(test._software[0].name)
    # e = ExpressSoftware('e', 100, 100)
