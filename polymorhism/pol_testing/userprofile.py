from polymorhism.pol_testing.abc_class import Abstract
import unittest


class User(Abstract):
    PRICE = 100

    def __init__(self, name, age):
        super().__init__(name, age)

    def show_name_capitalize(self):
        return self.name.title()

    def show_price(self):
        return self.__class__.PRICE


class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User('test', 39)

    def test_all_corect_set_up(self):
        self.assertEqual(self.user.name, 'test')
        self.assertEqual(self.user.age, 39)
        self.assertEqual(self.user.PRICE, 100)

    def test_parent_class(self):
        self.assertTrue(issubclass(User, Abstract))


if __name__ == '__main__':
    user = User('test', 39)
    print(user.show_name_capitalize())
    print(user.show_price())
    unittest.main()
