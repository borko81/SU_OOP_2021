import unittest

from polymorhism.project import Vehicle


class TestVehicle(unittest.TestCase):
    def setUp(self):
        self.car = Vehicle(100, 5)

    def test_attrib_assigned(self):
        self.assertEqual(self.car.fuel, 100)
        self.assertEqual(self.car.capacity, 100)
        self.assertEqual(self.car.horse_power, 5)
        self.assertEqual(self.car.fuel_consumption, self._Vehicle__DEFAULT_FUEL_CONSUMPTION)


if __name__ == '__main__':
    unittest.main()