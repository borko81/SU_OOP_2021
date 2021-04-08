import unittest

from project.battle_field import BattleField
from project.card.trap_card import TrapCard
from project.player.advanced import Advanced
from project.player.beginner import Beginner


class TestBattleField(unittest.TestCase):

    def setUp(self):
        self.b = BattleField()

    def test_fight_is_static(self):
        self.assertEqual(type(BattleField.fight).__name__, 'function')

    def test_fight_with_attacker_is_dead(self):
        a = Beginner('A')
        e = Beginner('A')
        a.health = 0
        with self.assertRaises(ValueError) as ex:
            self.b.fight(a, e)
        self.assertEqual(str(ex.exception), "Player is dead!")

    def test_fight_with_enemy_is_dead(self):
        a = Beginner('A')
        e = Beginner('A')
        e.health = 0
        with self.assertRaises(ValueError) as ex:
            self.b.fight(a, e)
        self.assertEqual(str(ex.exception), "Player is dead!")

    def test_attacker_increase_health_if_class_is_begginer(self):
        a = Beginner('A')
        e = Advanced('A')
        self.b.fight(a, e)
        self.assertEqual(a.health, 90)
        self.assertEqual(e.health, 250)

    def test_enemy_increase_health_if_class_is_begginer(self):
        a = Advanced('A')
        e = Beginner('A')
        self.b.fight(a, e)
        self.assertEqual(a.health, 250)
        self.assertEqual(e.health, 90)

    def test_helth_increase_beforo_fight_with_helth_of_card(self):
        a = Beginner('A')
        e = Advanced('AA')
        a.health = 1000
        # d- 120, h-5
        c_a = TrapCard('TrapCard')
        c_e = TrapCard('TrapCard')
        a.card_repository.cards.append(c_a)
        e.card_repository.cards.append(c_e)
        self.b.fight(a, e)
        self.assertEqual(sum(i.damage_points for i in a.card_repository.cards), 150)
        self.assertEqual(sum(i.damage_points for i in e.card_repository.cards), 120)
        self.assertEqual(a.health, 925)
        self.assertFalse(a.is_dead)
        self.assertFalse(e.is_dead)


    def test_helth_one_hero_die(self):
        a = Beginner('A')
        e = Advanced('AA')
        e.health = 1000
        # d- 120, h-5
        c_a = TrapCard('TrapCard')
        c_e = TrapCard('TrapCard')
        a.card_repository.cards.append(c_a)
        e.card_repository.cards.append(c_e)
        with self.assertRaises(ValueError) as ex:
            self.b.fight(a, e)
        self.assertEqual(str(ex.exception), "Player's health bonus cannot be less than zero.")

    def test_helth_one_hero_die2(self):
        a = Advanced('A')
        e = Advanced('AA')
        # d- 120, h-5
        c_a = TrapCard('TrapCard')
        c_a.damage_points = 255
        c_e = TrapCard('TrapCard')
        a.card_repository.cards.append(c_a)
        e.card_repository.cards.append(c_e)
        self.b.fight(a, e)
        self.assertTrue(e.is_dead)
        self.assertEqual(a.health, 255)


if __name__ == '__main__':
    unittest.main()
