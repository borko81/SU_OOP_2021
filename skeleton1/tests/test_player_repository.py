import unittest

from project.player.beginner import Beginner
from project.player.player_repository import PlayerRepository


class TestPlayerREpo(unittest.TestCase):
    def setUp(self):
        self.player_repo = PlayerRepository()

    def test_set_up(self):
        self.assertEqual(self.player_repo.count, 0)
        self.assertEqual(self.player_repo.players, [])

    def test_add_player(self):
        player = Beginner('Test')
        self.player_repo.add(player)
        self.assertEqual(self.player_repo.count, 1)
        self.assertEqual(self.player_repo.players[0], player)

    def test_add_player_when_player_exists_should_raise_exception(self):
        player = Beginner('Test')
        self.player_repo.add(player)
        with self.assertRaises(ValueError) as ex:
            self.player_repo.add(player)
        self.assertEqual(str(ex.exception), "Player Test already exists!")

    def test_find(self):
        player = Beginner('Test')
        self.player_repo.add(player)
        self.assertEqual(self.player_repo.find('Test'), player)

    def test_remove_player_when_exists(self):
        player = Beginner('Test')
        self.player_repo.add(player)
        self.player_repo.remove('Test')
        self.assertEqual(self.player_repo.count, 0)
        self.assertEqual(self.player_repo.players, [])

    def test_remove_player_when_name_is_empty(self):
        with self.assertRaises(ValueError) as ex:
            self.player_repo.remove('')
        self.assertEqual(str(ex.exception), "Player cannot be an empty string!")



if __name__ == '__main__':
    unittest.main()
