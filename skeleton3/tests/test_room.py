import unittest

from project.appliances.tv import TV
from project.rooms.alone_old import AloneOld
from project.rooms.alone_young import AloneYoung


class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room_alone_old = AloneOld('Old', 100)
        self.room_alone_young = AloneYoung('Young', 100)



    def test_set_up(self):
        self.assertEqual(self.room_alone_old.family_name, 'Old')
        self.assertEqual(self.room_alone_old.budget, 100)
        self.assertEqual(self.room_alone_old.members_count, 1)
        self.assertEqual(self.room_alone_old.children, [])
        self.assertListEqual([i.__class__.__name__ for i in self.room_alone_young.appliances], ['TV'])

    def test_calculate_expenes_alone_old(self):
        self.assertEqual(self.room_alone_old.expenses, 0)

    def test_room_alone_young_expenses(self):
        self.assertEqual(self.room_alone_young.room_cost, 10)
        self.assertEqual(self.room_alone_young.calculate_expenses(self.room_alone_young.appliances), 1.5)

    def test_expenses_should_raise_exception_when_less_then_zero(self):
        with self.assertRaises(ValueError) as ex:
            self.room_alone_old.expenses = -10
        self.assertEqual(str(ex.exception), "Expenses cannot be negative")
        self.assertEqual(self.room_alone_old.expenses, 0)

    def test_expenses_change_when_valid_value_input(self):
        self.room_alone_old.expenses = 10
        self.assertEqual(self.room_alone_old.expenses, 10)




if __name__ == '__main__':
    unittest.main()
