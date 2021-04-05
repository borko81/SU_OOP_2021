import unittest
import inspect
try:
    from uniitesting.dev.reduce import reduce
except ImportError:
    from dev.reduce import reduce



class TestReduse(unittest.TestCase):
    def test_01(self):
        """
        Check reduce method
        :return:
        """
        print(inspect.stack()[0][3])
        print(self.id())
        print(self.shortDescription())
        actual = reduce(10, 3)
        expected = 8
        self.assertNotEqual(expected, actual)

    def test_02(self):
        """
        Chack all is done
        :return:
        """
        print(inspect.stack()[0][3])
        print(self.id())
        print(self.shortDescription())
        actual = reduce(10, 3)
        expected = 7
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main(verbosity=2)
