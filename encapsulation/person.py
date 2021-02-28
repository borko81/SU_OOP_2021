class Person:
    def __init__(self, name: str, age: int):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age


if __name__ == "__main__":
    import unittest

    class TestPerson(unittest.TestCase):
        def setUp(self):
            self.user = Person("George", 39)

        def test_get_private_name(self):
            self.assertEqual(self.user.get_name(), "George")

        def test_get_private_age(self):
            self.assertEqual(self.user.get_age(), 39)

    unittest.main()
