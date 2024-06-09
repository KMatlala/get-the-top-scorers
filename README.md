
# Top Scorers Finder

## Description

This project is a Python program that takes a CSV file listing people and the score they achieved in a test, and outputs the top scorers along with their marks. If there are multiple top scorers, the program outputs all of them in alphabetical order.

## Features

- Parses CSV data.
- Identifies the top scorers and outputs their names and scores.

## Requirements

- Python 3.x

## Installation

1. Clone the repository or download the script.
2. Ensure you have Python 3.x installed on your machine.

## Usage

1. Prepare your CSV file with the following format:

    ```
    First Name,Second Name,Score
    Dee,Moore,56
    Sipho,Lolo,78
    Noosrat,Hoosain,64
    George,Of The Jungle,78
    Thandi,Ngcobo,45
    Mandla,Zulu,67
    Nomsa,Dlamini,78
    Sipho,Khumalo,82
    Bongani,Mthethwa,59
    Zanele,Sithole,72
    Sibusiso,Masango,88
    Lindiwe,Shabangu,74
    Andile,Ntuli,63
    Nokuthula,Mkhize,91
    Themba,Mhlongo,85
    Nokwazi,Ndaba,69
    Mfundo,Majola,77
    Nomvelo,Khumalo,66
    Sanele,Duma,73
    Mbali,Hlongwane,80
    Thabo,Gumede,57
    Nonhlanhla,Mhlongo,79
    Jabulani,Buthelezi,65
    Gugulethu,Ndlela,83
    Nkosinathi,Mabaso,60
    ```

2. Save the CSV file, for example, as `TestData.csv`.
3. Run the script from the command line:

    ```bash
    python top_scorers.py TestData.csv
    ```

4. The script will output the top scorers and their scores, and log the process.

## Example

Given the following `data/TestData.csv`:

```
First Name,Second Name,Score
Dee,Moore,56
Sipho,Lolo,78
Noosrat,Hoosain,64
George,Of The Jungle,78
Thandi,Ngcobo,45
Mandla,Zulu,67
Nomsa,Dlamini,78
Sipho,Khumalo,82
Bongani,Mthethwa,59
Zanele,Sithole,72
Sibusiso,Masango,88
Lindiwe,Shabangu,74
Andile,Ntuli,63
Nokuthula,Mkhize,91
Themba,Mhlongo,85
Nokwazi,Ndaba,69
Mfundo,Majola,77
Nomvelo,Khumalo,66
Sanele,Duma,73
Mbali,Hlongwane,80
Thabo,Gumede,57
Nonhlanhla,Mhlongo,79
Jabulani,Buthelezi,65
Gugulethu,Ndlela,83
Nkosinathi,Mabaso,60
```

Run:
```bash
python data/TestData.csv
```

The output will be:

```
Top scorers with score 91:
Nokuthula Mkhize: 91
```

## Logging

The script uses the standard Python `logging` module to log debug and information messages. The logging configuration is set up to output logs to the console.