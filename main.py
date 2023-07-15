import csv

statement_file = '/Users/surajan/Downloads/june2023.csv'


class Record:
    def __init__(self, description, date, debit, credit, record_type):
        self.description = description
        self.date = date
        self.debit = debit
        self.credit = credit
        self.type = record_type


def readCSV(filePath):
    records = []
    with open(filePath) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        row_number = 0
        for row in csv_reader:
            if row_number >= 2:
                description = row[1]
                debit = row[3]
                credit = row[4]
                records.append(Record(description,row[2], debit, credit, 'EXPENSE'))
                # print(f'{row_number} -> {row[1]} -> {row[2]} -> {row[3]} -> {row[4]}')
            row_number += 1
    print (len(records))

    sum = 0.00
    for record in records:
        if float(record.debit) <= 5000:
            sum = sum + float(record.debit)
            print (f'{record.description} = {record.debit}')
    print(sum)


if __name__ == '__main__':
    readCSV(statement_file)
