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
        self.id = id
        self.assignment = assignment
        self.grade = grade

    def get_id(self) -> int:
        return self.id

    def get_grade(self) -> float:
        return self.grade

    def get_assignment(self) -> Assignment:
        return self.assignment


class Student:

    def __init__(self, id: int, first_name: str, last_name: str, town: str):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.town = town

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
        grades_ls = []
        grades_ls.sort()
        lowest_number = grades_ls[0]
        avg = sum(grades_ls)-lowest_number
        return avg

    # def assign(self, assignment: Assignment) -> AssignmentResult:
