"""
This module is responsible for processing the data.  It will largely contain functions that will receive the overall dataset and
perform necessary processes in order to provide the desired result in the desired format.
It is likely that most sections will require functions to be placed in this module.
"""


import csv

def load_csv(file_path):

    data = []
    try:
        with open ('C:\\Users\\Joao Victor\\Downloads\\project_template\\data\\disneyland_reviews.csv', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                data.append(row)
        print(f"\nSuccessfully loaded {len(data)} rows")
    except FileNotFoundError:
        print("File not found")
    return data

if __name__ == "__main__":
    file_path = r'C:\Users\Joao Victor\Downloads\project_template\data\disneyland_reviews.csv'
    data = load_csv(file_path)