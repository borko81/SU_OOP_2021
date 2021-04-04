import unittest

from project.factory.factory import Factory
from project.factory.paint_factory import PaintFactory


class TestPaintFactory(unittest.TestCase):
    def setUp(self):
        self.paint = PaintFactory('Paint', 100)

    def test_all_set_up(self):
        self.assertEqual(self.paint.name, 'Paint')
        self.assertEqual(self.paint.capacity, 100)
        self.assertEqual(self.paint.valid_ingredients, ["white", "yellow", "blue", "green", "red"])
        self.assertEqual(self.paint.ingredients, {})

    def test_ingredianet_not_in_default(self):
        self.assertTrue('black' not in self.paint.valid_ingredients)

    def test_ingrediant_in_default(self):
        self.assertTrue('yellow' in self.paint.valid_ingredients)


    def test_add_ingrediant_when_not_valid_type_should_raise_error(self):
        with self.assertRaises(TypeError) as ex:
            self.paint.add_ingredient('black', 100)
        self.assertEqual(str(ex.exception), "Ingredient of type black not allowed in PaintFactory")

    def test_add_ingrediant_when_capacity_less_then_quantity_should_raise_error(self):
        with self.assertRaises(ValueError) as ex:
            self.paint.add_ingredient('white', 150)
        self.assertEqual(str(ex.exception), "Not enough space in factory")

    def test_add_ingrediant_not_in_ing_type_add_to_dict_with_tpes(self):
        self.paint.add_ingredient('white', 50)
        self.assertEqual(self.paint.ingredients['white'], 50)

    def test_add_to_ingrediant_secod_type(self):
        self.paint.add_ingredient('white', 50)
        self.paint.add_ingredient('white', 50)
        self.assertEqual(self.paint.ingredients['white'], 100)

    def test_remove_ingrediant_when_type_not_in_keys_should_raise_error(self):
        with self.assertRaises(KeyError) as ex:
            self.paint.remove_ingredient('white', 50)
        self.assertEqual(str(ex.exception), "'No such product in the factory'")

    def test_remove_ingrediant_succesfully_reduce_quntity(self):
        self.paint.add_ingredient('white', 50)
        self.paint.remove_ingredient('white', 50)
        self.assertEqual(self.paint.ingredients['white'], 0)

    def test_remove_ingrediant_with_big_quantity_should_raise_error(self):
        self.paint.add_ingredient('white', 50)
        with self.assertRaises(ValueError) as ex:
            self.paint.remove_ingredient('white', 60)
        self.assertEqual(str(ex.exception), "Ingredient quantity cannot be less than zero")

    def test_paint_is_not_abstract_and_inheritfrom(self):
        self.assertTrue(issubclass(PaintFactory, Factory))

    def test_product(self):
        self.assertEqual(self.paint.ingredients, {})
        self.paint.add_ingredient('white', 50)
        self.assertEqual(self.paint.products, {'white': 50})

    def test_cann_add(self):
        self.paint.add_ingredient('white', 90)
        actual = self.paint.can_add(20)
        self.assertEqual(actual, False)

    def test_cannot_instnces(self):
        with self.assertRaises(TypeError):
            Factory('test', 100)

    def test_add_ingrediant_is_abstract(self):
        with self.assertRaises(TypeError):
            Factory('test', 100).add_ingredient('white', 10)

    def test_repr(self):
        self.paint.add_ingredient('white', 50)
        self.assertEqual(str(self.paint), 'Factory name: Paint with capacity 100.\nwhite: 50\n')

    def test_implement_all_abstract(self):
        self.assertNotEqual(self.paint, 'TypeError:')

    def test_add_multi(self):
        self.paint.add_ingredient('white', 50)
        self.paint.add_ingredient('white', 50)
        self.paint.add_ingredient('white', 50)
        self.assertEqual(self.paint.ingredients['white'], 150)

if __name__ == '__main__':
    unittest.main()