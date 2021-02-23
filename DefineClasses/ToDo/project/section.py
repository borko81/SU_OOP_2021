import unittest

class Section:

    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, new_task):
        if new_task in self.tasks:
            return f'Task is already in the section {self.name}'
        self.tasks.append(new_task)
        return f'Task {new_task.details()} is added to the section'

    def complete_task(self, task_name: str):
        temp_task = [x for x in self.tasks if x.name == task_name]
        if not temp_task:
            return f"Could not find task with the name {task_name}"
        temp_task[0].completed = True
        return f"Completed task {task_name}"

    def clean_section(self):
        clean_task = [x for x in self.tasks if x.completed]
        self.tasks = [x for x in self.tasks if not x.completed]
        return f'Cleared {len(clean_task)} tasks.'

    def view_section(self):
        data = f'Section {self.name}:\n'
        for task in self.tasks:
            data += task.details() + '\n'
        return data


class TestSection(unittest.TestCase):
    def setUp(self):
        self.sec = Section('first section')

    def test_all_param_is_set_correct(self):
        self.assertEqual(self.sec.name, 'first section')

if __name__ == '__main__':
    unittest.main()