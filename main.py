import csv

statement_file = '/Users/surajan/Documents/reader-dump/june2022.txt'


def readCSV(filePath):
    with open(filePath) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        row_number = 0
        for row in csv_reader:
            if row_number >= 2:
                print(f'{row_number} -> {row[1]} -> {row[3]} -> {row[4]}')
            row_number += 1


if __name__ == '__main__':
    readCSV(statement_file)
