class Assignment:

    def __init__(self, name: str, difficulty: float):
        self.name = name
        self.difficulty = difficulty

    def get_name(self) -> str:
        return self.name

    def get_difficulty(self) -> float:
        return self.difficulty

    def __str__(self) -> str:
        return self.name


class AssignmentResult:

    def __init__(self, id: int, assignment: Assignment, grade: float):
        self.assignment_id = id
        self.assignment = assignment
        self.assignment_grade = grade

    def get_id(self) -> int:
        return self.assignment_id

    def get_grade(self) -> float:
        return self.assignment_grade

    def get_assignment(self) -> Assignment:
        return self.assignment


class Student:

    def __init__(self, id: int, first_name: str, last_name: str, town: str):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.town = town
        self.grades_ls = []
        self.energy = 1

    def get_id(self) -> int:
        return self.id

    def get_first_name(self) -> str:
        return self.first_name

    def set_first_name(self, first_name):
        self.first_name = first_name

    def get_last_name(self) -> str:
        return self.last_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def get_town(self) -> str:
        return self.town

    def set_town(self, town):
        self.town = town

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def get_grade(self) -> float:
        grades_ls = self.grades_ls.copy()
        if len(grades_ls) >= 2:
            lowest_grade = min(grades_ls)
            grades_ls.remove(lowest_grade)
            # also made a change here
        elif len(self.grades_ls) == 0:
            return 0
        elif len(self.grades_ls) == 1:
            return self.grades_ls[0]

        average = sum(grades_ls) / len(grades_ls)
        # / does not pass Test Full
        # / does not pass get median grade
        # / does not pass get min grade
        return average

    def assign(self, assignment: Assignment) -> AssignmentResult:
        a_grade = 1 - self.energy * assignment.difficulty
        if a_grade < 0:
            a_grade = 0

        self.grades_ls.append(a_grade)
        self.grades_ls.sort()
        self.energy = self.energy - self.energy * assignment.difficulty

        assignment_res = AssignmentResult(self.id, assignment, a_grade)
        return assignment_res

    def sleep(self, hours: float):
        self.energy = min((1, self.energy * (1 + hours / 10)))

    def get_energy(self):
        if self.energy < 0:
            self.energy = 0
        return self.energy


class Course:
    def __init__(self, students: list):
        self.students = list(students)

    def get_mean_grade(self) -> float:
        total = 0  # init total
        number_count_of_grades = 0  # init count of grades within a given course
        for student in self.students:  # for loop
            number_count_of_grades += len(student.grades_ls)  # add the count of grades received to this var
            total += student.get_grade()  # for each grade received add to the total
        return total / number_count_of_grades  # return the average

    def get_max_grade(self):
        max_grade = 0
        for student in self.students:
            student_max_grade = max(student.grades_ls)
            if student_max_grade > max_grade:
                max_grade = student_max_grade
        return max_grade

    def get_min_grade(self):  # issue here
        min_grade = 0
        for student in self.students:
            student_min_grade = min(student.grades_ls)
            if student_min_grade < min_grade:
                min_grade = student_min_grade
        return min_grade

    def get_median_grade(self) -> float:  # issue here
        grades = []

        for student in self.students:
            for i in student.grades_ls:
                grades.append(i)
        grades.sort()

        if len(grades) % 2 != 0:
            return grades[len(grades) // 2]

        return (grades[len(grades) // 2] + grades[len(grades) // 2 + 1]) / 2

    def get_grade_variance(self) -> float:
        mean = self.get_mean_grade()
        total = 0
        score_counts = 0
        for student in self.students:
            score_counts += len(student.grades_ls)
            for grade in student.grades_ls:
                total += (grade - mean) ** 2
        return total / score_counts

    def get_grade_std_dev(self) -> float:
        return self.get_grade_variance() ** (1 / 2)

    def assign(self, name: str, difficulty: float):
        assignment = Assignment(name, difficulty)
        for student in self.students:
            student.assignment_res = student.assign(assignment)
        return None
