from collections import namedtuple

Student = namedtuple("Student", ["name", "age"])

names = ["Jonh", "Mar", "Borko"]
ages = [30, 38, 39]

students = [
    Student(*details) for details in zip(names, ages)
]

max_age_student = max(students, key=lambda x: x.age)

print("{max_age_student.name} has {max_age_student.age} old")
