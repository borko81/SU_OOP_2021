import unittest

from project.battle_field import BattleField
from project.card.card_repository import CardRepository
from project.card.magic_card import MagicCard
from project.player.advanced import Advanced
from project.player.beginner import Beginner


class TestBattleField(unittest.TestCase):

    def setUp(self):
        self.bf = BattleField()

    def test_fight_any_is_dead(self):
        p1 = Beginner('One')
        p2 = Beginner('Two')
        p1.health = 0
        with self.assertRaises(ValueError) as ex:
            self.bf.fight(p1, p2)
        self.assertEqual(str(ex.exception), "Player is dead!")
    #
    # def test_is_player_is_begginer(self):
    #     p1 = Beginner('One')
    #     p2 = Beginner('Two')
    #     card = CardRepository()
    #     c = MagicCard('test')
    #     card.add(c)
    #     self.bf.fight(p1, p2)
    #     self.assertEqual(p1.health, 90)
    #     self.assertEqual(p2.health, 90)
    #     self.assertEqual(p1.card_repository.cards, 0)

    def test_dammage_and_healthy_wihtout_card(self):
        p1 = Beginner('One')
        p2 = Advanced('Two')
        self.bf.fight(p1, p2)
        self.assertEqual(p1.health, 90)
        self.assertEqual(p2.health, 250)

    def test_damage_and_health_with_cards(self):
        p1 = Beginner('One')
        p2 = Advanced('Two')
        p1.card_repository.add(MagicCard('magic1'))
        p2.card_repository.add(MagicCard('magic2'))
        self.bf.fight(p1, p2)

        self.assertEqual(p1.health, 165)
        self.assertEqual(p2.health, 295)


if __name__ == '__main__':
    unittest.main()
