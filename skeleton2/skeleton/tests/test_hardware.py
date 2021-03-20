import unittest

from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware



class TestHardware(unittest.TestCase):
    def setUp(self):
        self.hardware = HeavyHardware('test', 100, 512)
        self.power = PowerHardware('test', 100, 512)

    def test_setup_heavy(self):
        self.assertEqual(self.hardware.name, 'test')
        self.assertEqual(self.hardware.type, 'Heavy')
        self.assertEqual(self.hardware.capacity, 200)
        self.assertEqual(self.hardware.memory, 384)
        self.assertEqual(self.hardware.software_components, [])

    def test_setup_power(self):
        self.assertEqual(self.power.name, 'test')
        self.assertEqual(self.power.type, 'Power')
        self.assertEqual(self.power.capacity, 25)
        self.assertEqual(self.power.memory, 896)
        self.assertEqual(self.power.software_components, [])

    def test_install_when_is_ok_heavy(self):
        s = LightSoftware('Light', 10, 10)
        p = ExpressSoftware('Express', 10, 10)

        self.hardware.install(s)
        self.assertEqual(self.hardware.software_components[0], s)

        self.power.install(p)
        self.assertEqual(self.power.software_components[0], p)

    def test_install_when_not_good_param_heavy(self):
        s = LightSoftware('Light', 200, 384)
        p = ExpressSoftware('Express', 10, 900)

        with self.assertRaises(Exception) as ex:
            self.hardware.install(s)
        self.assertEqual(str(ex.exception), "Software cannot be installed")

        with self.assertRaises(Exception) as ex:
            self.power.install(p)
        self.assertEqual(str(ex.exception), "Software cannot be installed")

    def test_install_when_space_is_less_heavy(self):
        s = LightSoftware('Light', 10, 1000)
        with self.assertRaises(Exception) as ex:
            self.hardware.install(s)
        self.assertEqual(str(ex.exception), "Software cannot be installed")

    def test_install_when_space_and_memory_is_less_heavy(self):
        s = LightSoftware('Light', 100, 1000)
        with self.assertRaises(Exception) as ex:
            self.hardware.install(s)
        self.assertEqual(str(ex.exception), "Software cannot be installed")

    def test_uninstall_software_heavy(self):
        s = LightSoftware('Light', 10, 10)
        self.hardware.install(s)
        self.hardware.uninstall(s)
        self.assertEqual(self.hardware.software_components, [])

    def test_get_light_software_component_count(self):
        s = LightSoftware('Light', 10, 10)
        self.hardware.install(s)
        excpected = self.hardware.get_light_software_components_count()
        self.assertEqual(excpected, 1)

    def test_get_express_software_components_count(self):
        s = ExpressSoftware('Express', 10, 10)
        self.hardware.install(s)
        excpected = self.hardware.get_express_software_components_count()
        self.assertEqual(excpected, 1)




if __name__ == '__main__':
    unittest.main()
