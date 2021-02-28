class Account:
    def __init__(self, id, balance, pin):
        self.__id = id
        self.balance = balance
        self.__pin = pin

    def get_id(self, pin):
        if not pin == self.__pin:
            return "Wrong pin"
        return self.__id

    def change_pin(self, old_pin, new_pin):
        if not old_pin == self.__pin:
            return "Wrong pin"
        self.__pin = new_pin
        return "Pin changed"


if __name__ == '__main__':
    import unittest

    class TestAccount(unittest.TestCase):
        def setUp(self):
            self.acc = Account(1, 100, 123)

        def test_get_id_with_correct(self):
            expected = 1
            actual = self.acc.get_id(self.acc._Account__pin)
            self.assertEqual(expected, actual)

        def test_get_id_without_correct_value(self):
            expected = 'Wrong pin'
            self.assertEqual(expected, self.acc.get_id(100))

        def test_change_correct_pin(self):
            expected = 'Pin changed'
            actual = self.acc.change_pin(self.acc._Account__pin, 100)
            self.assertEqual(expected, actual)
            self.assertEqual(self.acc._Account__pin, 100)

        def test_change_pin_with_uncorect_value(self):
            self.assertEqual('Wrong pin', self.acc.change_pin(100, 100))

    unittest.main()
