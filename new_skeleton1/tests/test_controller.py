import unittest

from project.card.magic_card import MagicCard
from project.card.trap_card import TrapCard
from project.controller import Controller
from project.player.beginner import Beginner


class TestController(unittest.TestCase):
    def setUp(self) -> None:
        self.c = Controller()

    def test_all_setup_corect(self):
        self.assertEqual(self.c.player_repository.__class__.__name__, 'PlayerRepository')
        self.assertEqual(self.c.card_repository.__class__.__name__, 'CardRepository')

    def test_add_player(self):
        actual = self.c.add_player('Beginner', 'Borko')
        self.assertEqual(actual, "Successfully added player of type Beginner with username: Borko")
        self.assertEqual(self.c.player_repository.players[0].username, 'Borko')

        advanced_player = self.c.add_player("Advanced", 'Ad')
        self.assertEqual(advanced_player, "Successfully added player of type Advanced with username: Ad")
        self.assertEqual(self.c.player_repository.players[1].username, 'Ad')
        self.assertEqual(len(self.c.player_repository.players), 2)

    def test_add_card(self):
        magic_card = self.c.add_card('Magic', 'M')
        self.assertEqual(magic_card, "Successfully added card of type Magic with name: M")
        self.assertEqual(len(self.c.card_repository.cards), 1)
        self.assertEqual(self.c.card_repository.cards[0].name, 'M')

        trap_card = self.c.add_card('TrapCard', 'T')
        self.assertEqual(trap_card, "Successfully added card of type TrapCard with name: T")
        self.assertEqual(len(self.c.card_repository.cards), 2)
        self.assertEqual(self.c.card_repository.cards[1].name, 'T')

    def test_add_player_card(self):
        self.c.add_player('Beginner', 'B')
        self.c.add_card('TrapCard', 'T')
        actual = self.c.add_player_card('B', 'T')
        self.assertEqual(actual, "Successfully added card: T to user: B")
        self.assertEqual(len(self.c.player_repository.players[0].card_repository.cards), 1)

    def test_find(self):
        self.c.add_player('Advanced', 'A1')
        self.c.add_player('Advanced', 'A2')
        actual = self.c.fight('A1', 'A2')
        self.assertEqual(actual, 'Attack user health 250 - Enemy user health 250')

    def test_report(self):
        self.c.add_player('Advanced', 'A1')
        card = MagicCard('M')
        self.c.player_repository.players[0].card_repository.add(card)
        actual = self.c.report()
        self.assertEqual(actual, "Username: A1 - Health: 250 - Cards 1\n### Card: M - Damage: 5\n")




if __name__ == '__main__':
    unittest.main()
