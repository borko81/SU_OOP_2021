import unittest

from project.mammal import Mammal


class TestMammal(unittest.TestCase):
    def setUp(self):
        self.animal = Mammal('name', 'cat', 'meow')

    def test_all_set_up(self):
        self.assertEqual(self.animal.name, 'name')
        self.assertEqual(self.animal.type, 'cat')
        self.assertEqual(self.animal.sound, 'meow')
        self.assertEqual(self.animal._Mammal__kingdom, 'animals')

    def test_make_sound(self):
        self.assertEqual(self.animal.make_sound(), f"name makes meow")

    def test_get_kingdom(self):
        self.assertEqual(self.animal.get_kingdom(), 'animals')

    def test_info_message(self):
        self.assertEqual(self.animal.info(), 'name is of type cat')



if __name__ == '__main__':
    unittest.main()