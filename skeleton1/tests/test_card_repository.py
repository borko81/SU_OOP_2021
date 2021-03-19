import unittest

from project.card.card_repository import CardRepository
from project.card.magic_card import MagicCard


class TestCardRepo(unittest.TestCase):

    def setUp(self):
        self.card = CardRepository()

    def test_add_card_when_is_not_in_card(self):
        card = MagicCard('magic')
        self.card.add(card)
        self.assertEqual(self.card.count, 1)
        self.assertEqual(len(self.card.cards), 1)

    def test_add_card_when_is_in_card(self):
        card = MagicCard('magic')
        self.card.add(card)
        self.assertEqual(self.card.count, 1)
        self.assertEqual(len(self.card.cards), 1)
        with self.assertRaises(ValueError) as ex:
            self.card.add(card)
        self.assertEqual(str(ex.exception), "Card magic already exists!")

    def test_remove_card_when_is_calid(self):
        card = MagicCard("Magic")
        self.card.add(card)
        self.card.remove('Magic')
        self.assertEqual(self.card.count, 0)
        self.assertEqual(len(self.card.cards), 0)

    def test_remove_when_not_valid_should_raise_exception(self):
        with self.assertRaises(ValueError) as ex:
            self.card.remove('')
        self.assertEqual(str(ex.exception), "Card cannot be an empty string!")

    def test_find(self):
        card = MagicCard('magic')
        self.card.add(card)
        self.assertEqual(self.card.find('magic'), card)

if __name__ == '__main__':
    unittest.main()
