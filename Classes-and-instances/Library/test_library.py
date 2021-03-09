import unittest

from polymorhism.project import Library
from polymorhism.project import User


class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.lib = Library()
        self.user = User(1, "Borko")

    def test_setup_param(self):
        self.assertEqual(self.lib.user_records, [])
        self.assertEqual(self.lib.books_available, {})
        self.assertEqual(self.lib.rented_books, {})

    def test_add_user_to_user_records(self):
        self.lib.add_user(self.user)
        self.assertEqual(len(self.lib.user_records), 1)
        self.assertEqual(self.lib.user_records[0].username, 'Borko')
        self.assertEqual(self.lib.add_user(self.user), f"User with id = {self.user.user_id} already registered in the library!")
        self.assertEqual(len(self.lib.user_records), 1)

    def test_remove_user(self):
        self.assertEqual(self.lib.remove_user(User(2, 'Test')), "We could not find such user to remove!")
        self.lib.remove_user(self.user)
        self.assertEqual(len(self.lib.user_records), 0)

    def test_change_username(self):
        self.lib.add_user(self.user)
        self.assertEqual(self.lib.change_username(1, 'Borko'), "Please check again the provided username - it should be different than the username used so far!")
        self.lib.add_user(User(2, 'Test'))
        self.assertEqual(self.lib.change_username(2, 'Borko'), "Username successfully changed to: %s for userid: %d" % ('Borko', 2))
        # with self.assertRaises(IndexError):
        #     self.lib.change_username(3, 'Test')
        self.assertEqual(self.lib.change_username(3, 'Borko'), "There is no user with id = %d!" % 3)



if __name__ == '__main__':
    unittest.main()
