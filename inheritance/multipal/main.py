# test person
import unittest

from polymorhism.project import Employee
from polymorhism.project import Person
from polymorhism.project import Teacher


class Tests(unittest.TestCase):
    def test_person(self):
        p = Person()
        res = p.sleep()
        self.assertEqual(res, "sleeping...")

    def test_empl(self):
        p = Employee()
        res = p.get_fired()
        self.assertEqual(res, "fired...")

    def test_teacher(self):
        p = Teacher()
        res = p.teach()
        self.assertEqual(res, "teaching...")
        parents = [x.__name__ for x in p.__class__.__bases__]
        self.assertTrue("Person" in parents)
        self.assertTrue("Employee" in parents)


if __name__ == "__main__":
    unittest.main()
