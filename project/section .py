# Section class

class Section:

    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, new_task):
        if new_task in self.tasks:
            return f"Task is already in section {self.name}"
        self.tasks.append(new_task)
        return f"Task {new_task.detail()} is added to the section"

    def complete_task(self, task_name: str):
        temp_task = [x for x in self.tasks if x.name == task_name][0]
        if not temp_task:
            return "Could not find task with the name %s" % task_name
        temp_task.completed = True

    def clean_section(self):
        clean_task = [x for x in self.tasks if x.completed]
        self.tasks = [x for x in self.tasks if not x.completed]
        return f"Cleared {len(clean_task)}"

    def view_section(self):
        result = ''
        result += f"Section {self.name}\n"
        for task in self.tasks:
            result += f'{task.details()}\n'
        return result
