# class EntertainmentDevice:
#     def connect_to_device_via_hdmi_cable(self, device): pass
#
#     def connect_to_device_via_rca_cable(self, device): pass
#
#     def connect_to_device_via_ethernet_cable(self, device): pass
#
#     def connect_device_to_power_outlet(self, device): pass
#

from abc import ABC, abstractmethod

class RcaConector(ABC):
    @abstractmethod
    def connect_to_device_via_rca_cable(self, device):
        pass


class HdmiConnector(ABC):
    @abstractmethod
    def connect_to_device_via_hdmi_cable(self, device):
        pass


class EthernetConnector(ABC):
    @abstractmethod
    def connect_to_device_via_ethernet_cable(self, device):
        pass


class PowerConnector(ABC):
    @abstractmethod
    def connect_device_to_power_outlet(self, device):
        pass


class Television(RcaConector, HdmiConnector):
    def connect_to_device_via_rca_cable(self, device):
        pass

    def connect_to_game_console(self, game_console):
        self.connect_to_device_via_hdmi_cable(game_console)

    def connect_to_device_via_hdmi_cable(self, device):
        pass


class dvd_player(HdmiConnector, PowerConnector):
    def connect_to_device_via_hdmi_cable(self, device):
        pass

    def connect_device_to_power_outlet(self, device):
        pass


class GameConsole(Television, EthernetConnector):
    def connect_to_device_via_rca_cable(self, device):
        pass

    def connect_to_router(self, router):
        self.connect_to_device_via_ethernet_cable(router)

    def connect_to_device_via_ethernet_cable(self, device):
        pass


class Router(EthernetConnector, PowerConnector):
    def connect_to_device_via_ethernet_cable(self, device):
        pass

    def connect_device_to_power_outlet(self, device):
        pass
