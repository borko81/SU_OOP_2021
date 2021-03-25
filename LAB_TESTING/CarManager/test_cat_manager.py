import unittest

from LAB_TESTING.CarManager.car_manager import Car


class TestCar(unittest.TestCase):
    def setUp(self):
        self.car = Car('Car', 'Shkoda', 1, 30)

    def test_set_up(self):
        self.assertEqual(self.car.make, 'Car')
        self.assertEqual(self.car.model, 'Shkoda')
        self.assertEqual(self.car.fuel_consumption, 1)
        self.assertEqual(self.car.fuel_capacity, 30)
        self.assertEqual(self.car.fuel_amount, 0)

    def test_make_return_result(self):
        self.assertEqual(self.car.make, 'Car')

    def test_make_setter_raise_exception_if_not_value(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ''
        self.assertEqual(str(ex.exception), "Make cannot be null or empty!")

    def test_make_setter_change_value(self):
        self.car.make = 'car'
        self.assertEqual(self.car.make, 'car')

    def test_model_should_raise_exception_when_is_empty(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ''
        self.assertEqual(str(ex.exception), "Model cannot be null or empty!")

    def test_model_change_when_value_is_not_empty(self):
        self.car.model = 'Opel'
        self.assertEqual(self.car.model, 'Opel')

    def test_fuel_consumption_return(self):
        self.assertEqual(self.car.fuel_consumption, 1)

    def test_fuel_consumption_raise_exception_if_value_is_less_or_equal_to_zero(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = 0
        self.assertEqual(str(ex.exception), "Fuel consumption cannot be zero or negative!")

        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = -10
        self.assertEqual(str(ex.exception), "Fuel consumption cannot be zero or negative!")

    def test_fuel_capacist(self):
        self.assertEqual(self.car.fuel_capacity, 30)

    def test_fuel_capacity_raise_ex_when_less_or_equal_to_zeor(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = 0
        self.assertEqual(str(ex.exception), "Fuel capacity cannot be zero or negative!")

        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = -10
        self.assertEqual(str(ex.exception), "Fuel capacity cannot be zero or negative!")

    def test_fuel_amount(self):
        self.assertEqual(self.car.fuel_amount, 0)

    def test_fuel_ammount_should_raise_exceptipon_when_is_less_then_zero(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -10
        self.assertEqual(str(ex.exception), "Fuel amount cannot be negative!")

    def test_fuel_ammount_change_when_not_less_then_zero(self):
        self.car.fuel_amount = 10
        self.assertEqual(self.car.fuel_amount, 10)

    def test_refuel_raise_exception_when_try_to_refuel_with_negative_or_zero_value(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(0)
        self.assertEqual(str(ex.exception), "Fuel amount cannot be zero or negative!")

        with self.assertRaises(Exception) as ex:
            self.car.refuel(-10)
        self.assertEqual(str(ex.exception), "Fuel amount cannot be zero or negative!")

    def test_refuel_change_value(self):
        self.car.refuel(10)
        self.assertEqual(self.car.fuel_amount, 10)

    def test_refuel_when_more_then_fuel_capacity_return_capacity_value(self):
        self.car.refuel(40)
        self.assertEqual(self.car.fuel_amount, 30)

    def test_drive_raise_exception_when_fuel_is_not_enought(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(100)
        self.assertEqual(str(ex.exception), "You don't have enough fuel to drive!")

    def test_drive_decrease_value_when_distance_is_ok_to_car(self):
        self.car.fuel_amount = 1
        self.car.drive(10)
        self.assertEqual(self.car.fuel_amount, 0.9)

if __name__ == '__main__':
    unittest.main()