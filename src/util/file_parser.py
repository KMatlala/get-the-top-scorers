from src.util.logger import logger
from typing import List
from src.models.person import Person

separators = [',', '|']

class FileParser:
    """
    Manually parses a text string into a list of Person objects.
    
    Methods:
        parse(data: str) -> List[Person]: Parses the text data and returns a list of Person objects.
    """
    
    @staticmethod
    def parse(data: str) -> List[Person]:
        logger.debug("Starting to parse text data")
        lines = data.strip().split('\n')
        people = []
        for line in lines[1:]:  # Skip header
            for sep in separators:
                if sep in line:
                    first_name, last_name, score = line.split(sep, 2) # Can add to existing separators
                    people.append(Person(first_name.strip(), last_name.strip(), int(score.strip())))
                    logger.debug(f"Parsed person: {first_name.strip()} {last_name.strip()} with score: {score.strip()}")
                    break
                else:
                    logger.error(f"Invalid line format: {line}")
        logger.debug("Finished parsing text data")
        return people