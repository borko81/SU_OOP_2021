import unittest

from project.card.card_repository import CardRepository
from project.card.trap_card import TrapCard


class TestCardrepo(unittest.TestCase):
    def setUp(self):
        self.repo = CardRepository()

    def test_set_up(self):
        self.assertEqual(self.repo.count, 0)
        self.assertEqual(self.repo.cards, [])

    def test_add_when_card_is_not_exists_then_add_to_repo_cards_increase_count(self):
        # name, 120, 5
        card = TrapCard('TrapCard')
        self.repo.add(card)
        self.assertEqual(self.repo.cards[0], card)
        self.assertEqual(self.repo.count, 1)
        self.assertEqual(self.repo.cards[0].damage_points, 120)
        self.assertEqual(self.repo.cards[0].health_points, 5)

    def test_add_card_with_exists_name_should_raise_error(self):
        card = TrapCard('TrapCard')
        self.repo.add(card)
        with self.assertRaises(ValueError) as ex:
            self.repo.add(card)
        self.assertEqual(str(ex.exception), 'Card TrapCard already exists!')
        self.assertEqual(self.repo.count, 1)

    def test_remove_when_name_equal_to_empty_should_raise_error(self):
        with self.assertRaises(ValueError) as ex:
            self.repo.remove('')
        self.assertEqual(str(ex.exception), "Card cannot be an empty string!")

    def test_remove_card_with_corect_name(self):
        card = TrapCard('TrapCard')
        self.repo.add(card)
        self.repo.remove('TrapCard')
        self.assertEqual(self.repo.count, 0)
        self.assertListEqual(self.repo.cards, [])

    def test_find(self):
        card = TrapCard('TrapCard')
        self.repo.add(card)
        self.assertEqual(self.repo.find('TrapCard'), card)

if __name__ == '__main__':
    unittest.main()
