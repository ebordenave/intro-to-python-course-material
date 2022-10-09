class StudentGroup:
    def __init__(self, name: str, difficulty: float):
        self.name = name
        self.difficulty = difficulty

    def set_name(self, name):
        self.name = name

    def get_difficulty(self):
        return self.difficulty

    def set_difficulty(self, difficulty):
        self.difficulty = difficulty

    def get_name(self) -> str:
        return self.name

    def get_difficulty(self) -> float:
        return self.difficulty


def __str__(self) -> str:
    """
    Returns the name of the assignment as specified in the constructor.
    :return: The assignment name
    """
