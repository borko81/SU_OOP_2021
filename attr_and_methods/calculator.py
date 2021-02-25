from functools import reduce
import unittest


class Calculator:

    @staticmethod
    def add(*args):
        return sum(args)

    @staticmethod
    def multiply(*args):
        return reduce(lambda x, y: x * y, args)

    @staticmethod
    def divide(*args):
        try:
            return reduce(lambda x, y: x / y, args)
        except ZeroDivisionError as e:
            raise e

    @staticmethod
    def subtract(*args):
        return reduce(lambda x, y: x - y, args)


class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(Calculator.add(5, 10, 4), 19)

    def test_multiply(self):
        self.assertEqual(Calculator.multiply(1, 2, 3, 5), 30)

    def test_divdie_without_zero(self):
        self.assertEqual(Calculator.divide(100, 2), 50)

    def test_divide_with_zero_should_return_exception(self):
        with self.assertRaises(ZeroDivisionError):
            Calculator.divide(100, 0)

    def test_substract(self):
        self.assertEqual(Calculator.subtract(-10, 5), -15)

    def test_methods_are_static(self):
        check = Calculator()
        methods = [check.add, check.multiply, check.divide, check.subtract]

        for met in methods:
            self.assertEqual(type(met).__name__, 'function')


if __name__ == '__main__':
    unittest.main()
