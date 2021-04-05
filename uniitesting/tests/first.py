import unittest
import inspect

'''Start with py first -v, to show name of classes'''


class TestCaseOne(unittest.TestCase):

    def test_case_01(self):
        """
        Test param is set correct
        :return:
        """
        print(inspect.stack()[0][3])
        my_str = 'Borko'
        my_age = 10
        self.assertTrue(isinstance(my_str, str))
        self.assertTrue(isinstance(my_age, int))

    def test_case_02(self):
        """
        Test validate value for pi
        :return:
        """
        print(inspect.stack()[0][3])
        pi = 3.14
        self.assertFalse(isinstance(pi, int))

    def test_case_03(self):
        """
        Test name is upper
        :return:
        """
        print(inspect.stack()[0][3])
        name = 'PYTHON'
        self.assertTrue(name.isupper())
        print(f"\nTest is name upper or not\n")


if __name__ == '__main__':
    unittest.main(verbosity=2)
