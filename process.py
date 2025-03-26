"""
This module is responsible for processing the data.  It will largely contain functions that will receive the overall dataset and
perform necessary processes in order to provide the desired result in the desired format.
It is likely that most sections will require functions to be placed in this module.

Author: Joao Victor Garcia Schiavo
Date: 31/12/2024
"""


import csv
import os


file_path = os.path.join(os.path.dirname(__file__), 'data', 'disneyland_reviews.csv')

def load_csv(path=file_path):
    data = []
    try:
        with open(path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
        print(f"\nSuccessfully loaded {len(data)} rows")
    except FileNotFoundError:
        print(f"File not found at path: {path}")
    return data


if __name__ == "__main__":
    data = load_csv(file_path)
