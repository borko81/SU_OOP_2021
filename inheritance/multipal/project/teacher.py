from polymorhism.project import Employee
from polymorhism.project import Person


class Teacher(Person, Employee):

    def teach(self):
        return 'teaching...'


if __name__ == '__main__':
    t = Teacher()
    print([x.__name__ for x in t.__class__.__bases__])