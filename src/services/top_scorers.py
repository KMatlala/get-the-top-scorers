from src.util.logger import logger
from typing import List, Tuple
from src.models.person import Person

class TopScorers:
    """
    Finds the top scorers from a list of Person objects.
    
    Methods:
        get_top_scorers(people: List[Person]) -> Tuple[List[Person], int]: Returns the top scorers and the highest score.
    """
    @staticmethod
    def get_top_scorers(people: List[Person]) -> Tuple[List[Person], int]:
        logger.debug("Calculating top scorers")
        if not people:
            logger.warning("No people data provided")
            return [], 0
        max_score = max(person.score for person in people)
        top_scorers = [person for person in people if person.score == max_score]
        top_scorers.sort(key=lambda person: (person.first_name, person.last_name))
        return top_scorers, max_score