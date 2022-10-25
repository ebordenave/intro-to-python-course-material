import random
import statistics


class Student:
    grade = 0

    def assign(self):
        self.grade = random.randint(1, 100)

    def get_grade(self):
        return self.grade


class Course:
    students = []

    def __init__(self, students) -> None:
        self.students = students

    def get_mean_grade(self):
        grades = [s.get_grade() for s in self.students]
        return statistics.mean(grades)


students = [Student() for _ in range(10)]

course = Course(students=students)

assert 0 == course.get_mean_grade()

for s in students:
    s.assign()

assert 0 != course.get_mean_grade()
