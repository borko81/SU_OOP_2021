import unittest
from project.student import Student


class TestStuden(unittest.TestCase):
    def setUp(self):
        self.student1 = Student('Borko')
        self.student2 = Student('Boris', {'python': ['one', 'two']})

    def test_all_set_up(self):
        self.assertEqual(self.student1.name, 'Borko')
        self.assertEqual(self.student1.courses, {})
        self.assertEqual(self.student2.name, 'Boris')
        self.assertEqual(self.student2.courses, {'python': ['one', 'two']})

    def test_enroll_course_name_if_in_courses(self):
        acqure = self.student2.enroll('python', ['three', 'four'], add_course_notes='N')
        self.assertEqual(self.student2.courses['python'], ['one', 'two', 'three', 'four'])
        self.assertEqual(acqure, "Course already added. Notes have been updated.")

    def test_enroll_course_name_if_not_in_courses(self):
        acqure = self.student2.enroll('Python', ['three'], add_course_notes='N')
        self.assertEqual(self.student2.courses['Python'], [])
        self.assertEqual(acqure, "Course has been added.")

    def test_add_course_notes_is_y(self):
        acquire = self.student2.enroll('Python', ['three'], add_course_notes='Y')
        self.assertEqual(acquire, "Course and course notes have been added.")
        self.assertEqual(self.student2.courses['Python'], ['three'])

    def test_add_course_notes_is_empty(self):
        acquire = self.student2.enroll('Python', ['three'])
        self.assertEqual(acquire, "Course and course notes have been added.")
        self.assertEqual(self.student2.courses['Python'], ['three'])


    def test_add_notes_if_course_is_valid_add(self):
        acquire = self.student2.add_notes('python', 'three')
        self.assertEqual(acquire, "Notes have been updated")
        self.assertEqual(self.student2.courses['python'], ['one', 'two', 'three'])

    def test_add_notes_if_not_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            acquire = self.student1.add_notes('Python', 'one')
        self.assertEqual(str(ex.exception), 'Cannot add notes. Course not found.')

    def testleave_course_if_course_is_valid_return_message(self):
        acquire = self.student2.leave_course('python')
        self.assertEqual(self.student2.courses, {})
        self.assertEqual(acquire, "Course has been removed")

    def test_leave_course_if_course_is_not_valid_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            acquire = self.student1.leave_course('python')
        self.assertEqual(str(ex.exception), "Cannot remove course. Course not found.")


if __name__ == '__main__':
    unittest.main()
