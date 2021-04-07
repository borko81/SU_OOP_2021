import unittest

from project.card.card_repository import CardRepository
from project.player.advanced import Advanced
from project.player.player import Player


class TestAdvanced(unittest.TestCase):
    def setUp(self):
        self.user = Advanced('name')

    def test_all_is_ok(self):
        self.assertEqual(self.user.username, 'name')
        self.assertEqual(self.user.health, 250)
        self.assertEqual(self.user.card_repository.__class__.__name__, CardRepository.__name__)
        self.assertFalse(self.user.is_dead)

    def test_advanced_is_inherit_from_player(self):
        self.assertTrue(issubclass(Advanced, Player))

    def test_not_valid_username(self):
        with self.assertRaises(ValueError) as ex:
            self.user.username = ''
        self.assertEqual(str(ex.exception), "Player's username cannot be an empty string.")

    def test_change_name_corect(self):
        self.user.username = 'borko'
        self.assertEqual(self.user.username, 'borko')

    def test_health_less_then_zero_should_raise_exception(self):
        with self.assertRaises(ValueError) as ex:
            self.user.health = -1
        self.assertEqual(str(ex.exception), "Player's health bonus cannot be less than zero.")

    def test_health_change_with_big_then_zero_value(self):
        self.user.health = 100
        self.assertEqual(self.user.health, 100)

    def test_is_dead(self):
        self.assertFalse(self.user.is_dead)
        self.user.health = 0
        self.assertTrue(self.user.is_dead)
        self.user.health = 100

    def test_take_damage_with_zero_value_should_raise_error(self):
        with self.assertRaises(ValueError) as ex:
            self.user.take_damage(-100)
        self.assertEqual(str(ex.exception), "Damage points cannot be less than zero.")

    def test_take_damage_decrease_health(self):
        self.user.take_damage(50)
        self.assertEqual(self.user.health, 200)


if __name__ == '__main__':
    unittest.main()
