import unittest

class Task:

    def __init__(self, name: str, due_date: str):
        self.name = name
        self.due_date = due_date
        self.comments = []
        self.completed = False

    def change_name(self, new_name: str):
        if new_name == self.name:
            return "Name cannot be the same."
        
        self.name = new_name
        return self.name

    def change_due_date(self, new_date: str):
        if new_date == self.due_date:
            return "Date cannot be the same."

        self.due_date = new_date
        return self.due_date

    def add_comment(self, comment: str):
        self.comments.append(comment)

    def edit_comment(self, comment_number: int, new_comment: str):
        if comment_number not in range(len(self.comments)):
            return "Cannot find comment."

        self.comments[comment_number] = new_comment
        return f"{', '.join(self.comments)}"

    def details(self) -> str:
        return f"Name: {self.name} - Due Date: {self.due_date}"


# class TestTasks(unittest.TestCase):
#     def setUp(self):
#         self.task = Task("Make bed", "27/05/2020")

#     def test_all_set_up(self):
#         self.assertEqual(self.task.name, 'Make bed')
#         self.assertEqual(self.task.due_date, '27/05/2020')

#     def test_change_name_is_different(self):
#         self.task.change_name('Bed make')
#         self.assertEqual(self.task.name, 'Bed make')

#     def test_change_name_is_same(self):
#         self.assertEqual(self.task.change_name('Make bed'), "Name cannot be the same.")

#     def test_change_due_date_with_different(self):
#         self.assertEqual(self.task.change_due_date('01/01/2021'), '01/01/2021')

#     def test_change_due_date_with_same(self):
#         self.assertEqual(self.task.change_due_date("27/05/2020"), "Date cannot be the same.")

#     def test_details(self):
#         self.assertEqual(self.task.details(), f"Name: {self.task.name} - Due Date: {self.task.due_date}")

if __name__ == '__main__':
    unittest.main()

