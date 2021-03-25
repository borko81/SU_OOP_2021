import unittest

# from LAB_TESTING.List.extended_list import IntegerList


class TestList(unittest.TestCase):
    def setUp(self):
        self.my_list = IntegerList(1, 2, 3)
        self.uncorrect_list = IntegerList(1, 22.1, 4)

    def test_all_is_setup_correct(self):
        # self.assertListEqual(self.my_list.get_data(), [1, 2, 3])
        self.test_get_date()

    def test_init_not_allowed_not_int(self):
        self.assertListEqual(self.uncorrect_list.get_data(), [1, 4])

    def test_get_date(self):
        self.assertListEqual(self.my_list.get_data(), [1, 2, 3])

    def test_add_should_raise_exception_when_any_element_is_not_int(self):
        excpected = "Element is not Integer"
        with self.assertRaises(ValueError) as ex:
            self.my_list.add(11.1)
        self.assertEqual(str(ex.exception), excpected)

    def test_correct_add_element_return_data(self):
        self.my_list.add(4)
        self.assertEqual(self.my_list.get_data(), [1, 2, 3, 4])

    def test_remove_index_shoudl_raise_when_index_is_not_valid(self):
        with self.assertRaises(IndexError) as ex:
            self.my_list.remove_index(3)
        self.assertEqual(str(ex.exception), "Index is out of range")

    def test_remove_index_when_index_is_valid_return_value_from_posiiton(self):
        actual = self.my_list.remove_index(2)
        self.assertListEqual(self.my_list.get_data(), [1, 2])
        self.assertEqual(actual, 3)

    def test_get_should_raise_exception_when_index_is_invalid(self):
        with self.assertRaises(IndexError) as ex:
            self.my_list.get(3)
        self.assertEqual(str(ex.exception), "Index is out of range")

        with self.assertRaises(IndexError) as ex:
            self.my_list.get(4)
        self.assertEqual(str(ex.exception), "Index is out of range")

    def test_get_when_index_is_valid(self):
        actual = self.my_list.get(2)
        self.assertEqual(actual, 3)

    def test_insert_should_raise_error_when_index_is_not_valid(self):
        with self.assertRaises(IndexError) as ex:
            self.my_list.insert(3, 1)
        self.assertEqual(str(ex.exception), "Index is out of range")

        with self.assertRaises(IndexError) as ex:
            self.my_list.insert(4, 1)
        self.assertEqual(str(ex.exception), "Index is out of range")

    def test_insert_should_raise_ex_when_param_is_not_int(self):
        with self.assertRaises(ValueError) as ex:
            self.my_list.insert(2, 1.1)
        self.assertEqual(str(ex.exception), "Element is not Integer")

    def test_insert_index_return_corect_value_from_corect_params(self):
        self.my_list.insert(2, 22)
        self.assertListEqual(self.my_list.get_data(), [1, 2, 22, 3])

    def test_get_biggest(self):
        self.assertEqual(self.my_list.get_biggest(), 3)

    def test_get_index(self):
        self.assertEqual(self.my_list.get_index(2), 1)



if __name__ == '__main__':
    unittest.main()
