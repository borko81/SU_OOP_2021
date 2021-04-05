import unittest
import inspect

from dev.code import add


class TestCode(unittest.TestCase):

    def test_01(self):
        """
        Check add from code script
        :return:
        """
        print(inspect.stack()[0][3])
        actual = add(10, 5)
        expected = 15
        self.assertEqual(expected, actual, 'add(10, 5) -> 16')


if __name__ == '__main__':
    unittest.main(verbosity=2)
