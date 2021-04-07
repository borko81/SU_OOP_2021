import unittest

from project.player.beginner import Beginner
from project.player.player_repository import PlayerRepository


class TestPlayerRepo(unittest.TestCase):
    def setUp(self):
        self.repo = PlayerRepository()

    def test_set_up(self):
        self.assertEqual(self.repo.count, 0)
        self.assertListEqual(self.repo.players, [])

    def test_addplayer_when_player_name_exists(self):
        p = Beginner("Borko")
        self.repo.add(p)
        with self.assertRaises(ValueError) as ex:
            self.repo.add(p)
        self.assertEqual(str(ex.exception), "Player Borko already exists!")

    def test_add_player_when_name_is_new(self):
        p = Beginner('Borko')
        self.repo.add(p)
        self.assertTrue(len(self.repo.players), 1)
        self.assertEqual(self.repo.count, 1)
        self.assertEqual(self.repo.players[0].username, 'Borko')

    def test_remove_when_name_is_net_defined_should_raise_error(self):
        p = Beginner('Borko')
        self.repo.add(p)
        with self.assertRaises(ValueError) as ex:
            self.repo.remove("")
        self.assertEqual(str(ex.exception), "Player cannot be an empty string!")

    def test_remove_when_name_is_ncorect_remove_user(self):
        p = Beginner('Borko')
        self.repo.add(p)
        self.repo.remove('Borko')
        self.assertEqual(len(self.repo.players), 0)
        self.assertEqual(self.repo.count, 0)

    def test_find(self):
        p = Beginner('Borko')
        self.repo.add(p)
        actual = self.repo.find('Borko')
        self.assertEqual(p, actual)


if __name__ == '__main__':
    unittest.main()
