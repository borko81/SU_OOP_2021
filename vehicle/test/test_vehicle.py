import unittest

from project.vehicle import Vehicle


class TestVehicle(unittest.TestCase):
    def setUp(self):
        self.car = Vehicle(100, 5)

    def test_attrib_assigned(self):
        self.assertEqual(self.car.fuel, 100)
        self.assertEqual(self.car.capacity, 100)
        self.assertEqual(self.car.horse_power, 5)
        self.assertEqual(self.car.fuel_consumption, 1.25)

    def test_drive_ok(self):
        self.car.drive(10)
        self.assertEqual(self.car.fuel, 87.5)

    def test_drive_not_ok(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(100)
        self.assertEqual(str(ex.exception), 'Not enough fuel')

    def test_refuel_is_ok(self):
        self.car.drive(5)
        self.car.refuel(5)
        self.assertEqual(self.car.fuel, 98.75)

    def test_refuel_is_not_ok_should_raise_exception(self):
        self.car.drive(5)
        with self.assertRaises(Exception) as ex:
            self.car.refuel(15)
        self.assertEqual(str(ex.exception), "Too much fuel")

    def test_string_method(self):
        self.assertEqual(self.car.__str__(), 'The vehicle has 5 horse power with 100 fuel left and 1.25 fuel consumption')




if __name__ == '__main__':
    unittest.main()