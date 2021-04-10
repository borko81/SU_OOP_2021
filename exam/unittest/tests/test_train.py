import unittest

from project.train.train import Train


class TestTrain(unittest.TestCase):
    def setUp(self):
        self.t = Train('T', 10)

    def test_all_setup(self):
        self.assertEqual(self.t.name, 'T')
        self.assertEqual(self.t.capacity, 10)
        self.assertListEqual(self.t.passengers, [])

    def test_add_passenger_when_not_seat_raise_error(self):
        self.t.passengers = [1, 1, 1]
        self.t.capacity = 3
        with self.assertRaises(ValueError) as ex:
            self.t.add('Borko')
        self.assertEqual(str(ex.exception), "Train is full")
        self.assertListEqual(self.t.passengers, [1, 1, 1])
        self.assertEqual(self.t.capacity, 3)

    def test_add_pasanger_when_name_exists(self):
        self.t.add('Borko')
        self.assertEqual(self.t.passengers, ['Borko'])
        with self.assertRaises(ValueError) as ex:
            self.t.add('Borko')
        self.assertEqual(str(ex.exception), "Passenger Borko Exists")
        self.assertListEqual(self.t.passengers, ['Borko'])
        self.assertEqual(self.t.capacity, 10)

    def test_add_pasangers_when_all_ok(self):
        actual = self.t.add('Borko')
        self.assertEqual(self.t.passengers, ['Borko'])
        self.assertEqual(actual, "Added passenger Borko")

    def test_remove_passenger_when_name_not_exists_should_raise_error(self):
        self.t.add('Borko')
        with self.assertRaises(ValueError) as ex:
            self.t.remove('bobo')
        self.assertEqual(str(ex.exception), "Passenger Not Found")
        self.assertEqual(self.t.passengers, ['Borko'])

    def test_remove_passenger_when_name_exists(self):
        self.t.add('Borko')
        self.assertEqual(self.t.passengers, ['Borko'])
        self.t.remove('Borko')
        self.assertEqual(self.t.passengers, [])

if __name__ == '__main__':
    unittest.main()
