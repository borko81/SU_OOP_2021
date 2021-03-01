class Mammal:
    __kingdom = 'animals'

    def __init__(self, name, type, sound):
        self.name = name
        self.type = type
        self.sound = sound

    def make_sound(self):
        return '{name} make sound'.format(name=self.name)

    def get_kingdom(self):
        return __class__.__kingdom

    def info(self):
        return "{name} is of type {type}".format(name=self.name, type=self.type)


if __name__ == '__main__':
    import unittest

    class TestMammal(unittest.TestCase):
        def setUp(self):
            self.mammal = Mammal("Dog", "Domestic", "Bark")

        def test_return_class_atribute(self):
            expected = 'animals'
            actual = self.mammal.get_kingdom()
            self.assertEqual(expected, actual)

        def test_make_sound(self):
            self.assertEqual('Dog make sound', self.mammal.make_sound())

        def test_info_method(self):
            self.assertEqual('Dog is of type Domestic', self.mammal.info())

    unittest.main()
