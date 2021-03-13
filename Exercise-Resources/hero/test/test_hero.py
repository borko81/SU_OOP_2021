import unittest

from project.hero import Hero


class TestHero(unittest.TestCase):
    def setUp(self):
        self.hero = Hero('Hero1', 2, 100, 50)
        self.user2 = Hero('Hero1', 2, 100, 50)
        self.user3 = Hero('Hero2', 2, 100, 50)
        self.user4 = Hero('Lost', 2, 100, 40)

    def test_all_set_up(self):
        self.assertEqual(self.hero.username, 'Hero1')
        self.assertEqual(self.hero.level, 2)
        self.assertEqual(self.hero.health, 100)
        self.assertEqual(self.hero.damage, 50)

    def test_battle_with_same_name_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.user2)
        self.assertEqual(str(ex.exception), "You cannot fight yourself")

    def test_battle_helth_is_less_thjen_zero(self):
        hero_test_with_zero = Hero('ZeroName', 1, 0, 100)
        with self.assertRaises(ValueError) as ex:
            hero_test_with_zero.battle(self.user3)
        self.assertEqual(str(ex.exception), "Your health is lower than or equal to 0. You need to rest")

    def test_battle_intruder_has_zero_health(self):
        hero_test_with_zero = Hero('ZeroName', 1, 10, 100)
        intruder_hero = Hero('ZeroName2', 1, 0, 100)
        with self.assertRaises(ValueError) as ex:
            hero_test_with_zero.battle((intruder_hero))
        self.assertEqual(str(ex.exception), f"You cannot fight {intruder_hero.username}. He needs to rest")

    def test_hero_and_intruder_has_less_then_zero(self):
        acquire = self.hero.battle(self.user3)
        self.assertEqual(acquire, 'Draw')

    def test_enemy_health_is_zero_after_battle(self):
        acquire = self.hero.battle(self.user4)
        self.assertEqual(acquire, 'You win')
        self.assertEqual(self.hero.level, 3)
        self.assertEqual(self.hero.health, 25)
        self.assertEqual(self.hero.damage, 55)

    def test_hero_health_is_zero_after_battle(self):
        acquire = self.user4.battle(self.hero)
        self.assertEqual(acquire, 'You lose')
        self.assertEqual(self.hero.level, 3)
        self.assertEqual(self.hero.health, 25)
        self.assertEqual(self.hero.damage, 55)

    def test_represent_method(self):
        acquire = f"Hero {self.hero.username}: {self.hero.level} lvl\n" \
               f"Health: {self.hero.health}\n" \
               f"Damage: {self.hero.damage}\n"

        self.assertEqual(str(self.hero), acquire)


if __name__ == '__main__':
    unittest.main()
