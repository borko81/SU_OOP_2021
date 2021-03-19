import unittest

from project.card.card_repository import CardRepository
from project.player.advanced import Advanced
from project.player.player import Player


class TestAdvanced(unittest.TestCase):
    def test_set_attr(self):
        a = Advanced('test')
        self.assertEqual(a.username, 'test')
        self.assertEqual(a.health, 250)
        self.assertEqual(a.card_repository.__class__.__name__, CardRepository.__name__)
        self.assertFalse(a.is_dead)

    def test_username_raises(self):
        with self.assertRaises(ValueError) as ex:
            a = Advanced("")
        self.assertEqual(str(ex.exception), "Player's username cannot be an empty string.")

    def test_username_change(self):
        a = Advanced("test")
        a.username = 'new name'
        self.assertEqual(a.username, 'new name')

    def test_helath_is_less_then_zero_return_raises(self):
        a = Advanced('test')
        with self.assertRaises(ValueError) as ex:
            a.health = -10
        self.assertEqual(str(ex.exception), 'Player\'s health bonus cannot be less than zero.')

    def test_take_health_more_then_zero(self):
        a = Advanced("test")
        a.health = 20
        self.assertEqual(a.health, 20)

    def test_take_damage_less_then_zero_return_raises(self):
        a = Advanced("test")
        with self.assertRaises(ValueError) as ex:
            a.take_damage(-1)
        self.assertEqual(str(ex.exception), "Damage points cannot be less than zero.")

    def test_take_damage_is_ok_value(self):
        a = Advanced("test")
        a.take_damage(50)
        self.assertEqual(a.health, 200)

    def test_is_dead(self):
        a = Advanced("test")
        self.assertFalse(a.is_dead)
        a.take_damage(250)
        self.assertTrue(a.is_dead)

    def test_advanced_is_parent_class(self):
        a = Advanced("test")
        self.assertTrue(issubclass(Advanced, Player))

if __name__ == '__main__':
    unittest.main()