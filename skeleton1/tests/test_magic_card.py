import unittest

from project.card.magic_card import MagicCard


class TestMagicCard(unittest.TestCase):
    def setUp(self):
        self.card = MagicCard('magic')

    def test_set_up(self):
        self.assertEqual(self.card.name, 'magic')
        self.assertEqual(self.card.damage_points, 5)
        self.assertEqual(self.card.health_points, 80)

    def test_correct_name(self):
        self.card.name = 'New name'
        self.assertEqual(self.card.name, 'New name')

    def test_incorect_name(self):
        with self.assertRaises(ValueError) as ex:
            self.card.name = ''
        self.assertEqual(str(ex.exception), "Card's name cannot be an empty string.")

    def test_damage_point_is_more_then_zero(self):
        self.card.damage_points = 10
        self.assertEqual(self.card.damage_points, 10)

    def test_damage_point_is_less_then_zero(self):
        with self.assertRaises(ValueError) as ex:
            self.card.damage_points = -10
        self.assertEqual(str(ex.exception), "Card's damage points cannot be less than zero.")

    def test_health_point_is_more_then_zero(self):
        self.card.health_points = 10
        self.assertEqual(self.card.health_points, 10)

    def test_health_point_is_less_then_zero(self):
        with self.assertRaises(ValueError) as ex:
            self.card.health_points = -10
        self.assertEqual(str(ex.exception), "Card's HP cannot be less than zero.")


if __name__ == '__main__':
    unittest.main()
