import logging as logger
import sys
from src.util.file_parser import FileParser
from src.services.top_scorers import TopScorers

def main(input_file: str):
    """
    Main function to read input from a file, find the top scorers, and print them.
    
    Args:
        input_file (str): The path to the input file containing the CSV data.
    """
    logger.info(f"Reading input file: {input_file}")
    try:
        with open(input_file, 'r') as file:
            data = file.read()
    except FileNotFoundError:
        logger.error(f"File not found: {input_file}")
        sys.exit(1)
    
    people = FileParser.parse(data)
    top_scorers, highest_score = TopScorers.get_top_scorers(people)
    
    for top_scorer in top_scorers:
        logger.info(f"{top_scorer.first_name} {top_scorer.last_name}")
    logger.info(f"Score: {highest_score}")
    
    # if len(top_scorers) == 0:
    #     logger.info("No top scorers found")
    # elif len(top_scorers) == 1:
    #     logger.info(f"The top scorer is {top_scorers[0].first_name} {top_scorers[0].last_name} with score {highest_score}. ")
    # else:
    #     logger.info(f"The top scorers are: {[person.last_name + ',' + person.first_name for person in top_scorers]} with score {highest_score}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        logger.error("Usage: python top_scorers.py <input_file>")
        sys.exit(1)
    else:
        main(sys.argv[1])
