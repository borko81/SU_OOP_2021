import unittest

from project.factory.factory import Factory
from project.factory.paint_factory import PaintFactory


class TestPainFactory(unittest.TestCase):
    def setUp(self):
        self.paint = PaintFactory('Paint', 10)
        self.paint.valid_ingredients = ["white", "yellow", "blue", "green", "red"]

    def test_set_up_corect(self):
        self.assertEqual(self.paint.name, 'Paint')
        self.assertEqual(self.paint.capacity, 10)
        self.assertListEqual(self.paint.valid_ingredients, ["white", "yellow", "blue", "green", "red"])
        self.assertEqual(self.paint.ingredients, {})

    def test_paint_is_inherit_from_factory(self):
        self.assertTrue(issubclass(PaintFactory, Factory))

    def test_add_ingredient_when_type_not_in_valid_should_raise_error(self):
        with self.assertRaises(TypeError) as ex:
            self.paint.add_ingredient('black', 1)
        self.assertEqual(str(ex.exception), "Ingredient of type black not allowed in PaintFactory")

    def test_add_ingredient_when_type_is_good_but_capacity_is_less_should_raise_error(self):
        with self.assertRaises(ValueError) as ex:
            self.paint.add_ingredient('white', 20)
        self.assertEqual(str(ex.exception), "Not enough space in factory")

    def test_add_ingredient_when_all_is_ok(self):
        self.paint.add_ingredient('white', 10)
        self.assertEqual(self.paint.ingredients['white'], 10)
        self.assertEqual(self.paint.capacity, 10)

    def test_add_ingr_when_values_and_capcity_is_less_then_value(self):
        self.paint.add_ingredient('white', 5)
        with self.assertRaises(ValueError) as ex:
            self.paint.add_ingredient('white', 6)
        self.assertEqual(str(ex.exception), "Not enough space in factory")

    def test_add_infredient_for_second_time(self):
        self.paint.add_ingredient('white', 3)
        self.assertEqual(self.paint.ingredients['white'], 3)
        self.paint.add_ingredient('white', 3)
        self.assertEqual(self.paint.ingredients['white'], 6)

    def test_remove_ingredient_when_type_not_iningredients_should_raise_error(self):
        with self.assertRaises(KeyError) as ex:
            self.paint.remove_ingredient('black', 10)
        self.assertEqual(str(ex.exception), "'No such ingredient in the factory'")

    def test_remove_ingredient_when_quanity_is_more_then_ingredianets_quantity_shoud_raise_error(self):
        self.paint.add_ingredient('white', 5)
        with self.assertRaises(ValueError) as ex:
            self.paint.remove_ingredient('white', 11)
        self.assertEqual(str(ex.exception), 'Ingredients quantity cannot be less than zero')

    def test_rempve_ingredient_all_param_is_good(self):
        self.paint.add_ingredient('white', 10)
        self.paint.remove_ingredient('white', 5)
        self.assertEqual(self.paint.ingredients['white'], 5)

    def test_products(self):
        self.paint.add_ingredient('white', 10)
        self.assertEqual(self.paint.products, {'white': 10})


if __name__ == '__main__':
    unittest.main()
