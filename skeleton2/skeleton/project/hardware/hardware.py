from project.software.software import Software


class Hardware:
    def __init__(self, name, type, capacity, memory: int):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []

    def install(self, software):
        if self.can_install(software):
            self.software_components.append(software)
        else:
            raise Exception("Software cannot be installed")

    def uninstall(self, software):
        if software in self.software_components:
            self.software_components.remove(software)

    def get_light_software_components_count(self):
        return len([s for s in self.software_components if s.type == "Light"])

    def get_express_software_components_count(self):
        return len([s for s in self.software_components if s.type == "Express"])

    def can_install(self, software):
        has_space = sum([s.capacity_consumption for s in self.software_components]) + software.capacity_consumption <= self.capacity
        has_memory = sum([s.memory_consumption for s in self.software_components]) + software.memory_consumption <= self.memory
        return has_memory and has_space

    def __repr__(self):
        result = [f"Hardware Component - {self.name}",
                  f"Express Software Components: {self.get_express_software_components_count()}",
                  f"Light Software Components: {self.get_light_software_components_count()}",
                  f"Memory Usage: {int(sum([s.memory_consumption for s in self.software_components]))} / {int(self.memory)}",
                  f"Capacity Usage: {int(sum([s.capacity_consumption for s in self.software_components]))} / {int(self.capacity)}",
                  f"Type: {self.type}",
                  f"Software Components: {', '.join([s.name for s in self.software_components]) if self.software_components else 'None'}"]

        return "\n".join(result)
