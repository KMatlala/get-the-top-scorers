from src.util.logger import logger

class Person:
    """
    Represents a person with a name and a score.
    
    Attributes:
        name (str): The name of the person.
        score (int): The score of the person.
    """
    def __init__(self, first_name: str, last_name: str, score: int):
        self.first_name = first_name
        self.last_name = last_name
        self.score = score

    def __str__(self):
        return f"{self.first_name} {self.last_name}: {self.score}"