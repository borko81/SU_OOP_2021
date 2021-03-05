from project.employee import Employee
from project.person import Person


class Teacher(Person, Employee):

    def teach(self):
        return 'teaching...'


if __name__ == '__main__':
    t = Teacher()
    print([x.__name__ for x in t.__class__.__bases__])