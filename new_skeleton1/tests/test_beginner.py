import unittest

from project.card.card_repository import CardRepository
from project.player.beginner import Beginner
from project.player.player import Player


class TestBeginer(unittest.TestCase):
    def test_set_attr(self):
        a = Beginner('test')
        self.assertEqual(a.username, 'test')
        self.assertEqual(a.health, 50)
        self.assertEqual(a.card_repository.__class__.__name__, CardRepository.__name__)
        self.assertFalse(a.is_dead)

    def test_username_raises(self):
        with self.assertRaises(ValueError) as ex:
            a = Beginner("")
        self.assertEqual(str(ex.exception), "Player's username cannot be an empty string.")

    def test_username_change(self):
        a = Beginner("test")
        a.username = 'new name'
        self.assertEqual(a.username, 'new name')

    def test_helath_is_less_then_zero_return_raises(self):
        a = Beginner('test')
        with self.assertRaises(ValueError) as ex:
            a.health = -10
        self.assertEqual(str(ex.exception), 'Player\'s health bonus cannot be less than zero.')

    def test_take_health_more_then_zero(self):
        a = Beginner("test")
        a.health = 20
        self.assertEqual(a.health, 20)

    def test_take_damage_less_then_zero_return_raises(self):
        a = Beginner("test")
        with self.assertRaises(ValueError) as ex:
            a.take_damage(-1)
        self.assertEqual(str(ex.exception), "Damage points cannot be less than zero.")

    def test_take_damage_is_ok_value(self):
        a = Beginner("test")
        a.take_damage(40)
        self.assertEqual(a.health, 10)

    def test_is_dead(self):
        a = Beginner("test")
        self.assertFalse(a.is_dead)
        a.take_damage(50)
        self.assertTrue(a.is_dead)

    def test_advanced_is_parent_class(self):
        self.assertTrue(issubclass(Beginner, Player))


if __name__ == '__main__':
    unittest.main()
