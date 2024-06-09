import unittest
import sys
import os

sys.path.append('src')

from src.models.person import Person
from src.util.file_parser import FileParser
from src.util.logger import logger
from src.services.top_scorers import TopScorers

class TestPerson(unittest.TestCase):

    def test_person_initialization(self):
        person = Person("John", "Doe", 30)
        self.assertEqual(person.first_name, "John")
        self.assertEqual(person.last_name, "Doe")
        self.assertEqual(person.score, 30)

    def test_person_str(self):
        person = Person("Jane", "Doe", 25)
        self.assertEqual(str(person), "Jane Doe: 25")

class TestTopScorers(unittest.TestCase):

    def test_get_top_scorers(self):
        person1 = Person("Alice", "Smith", 90)
        person2 = Person("Bob", "Brown", 95)
        person3 = Person("Charlie", "Davis", 95)
        people = [person1, person2, person3]
        top_scorers, max_score = TopScorers.get_top_scorers(people)
        self.assertEqual(max_score, 95)
        self.assertEqual(len(top_scorers), 2)
        self.assertEqual(top_scorers[0].first_name, "Bob")
        self.assertEqual(top_scorers[1].first_name, "Charlie")

    def test_get_top_scorers_no_people(self):
        top_scorers, max_score = TopScorers.get_top_scorers([])
        self.assertEqual(max_score, 0)
        self.assertEqual(top_scorers, [])

if __name__ == '__main__':
    unittest.main()
