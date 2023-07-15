import csv

from record import Record

statement_file = '/Users/surajan/Downloads/june2023.csv'


def read_csv(file_path):
    records = []
    with open(file_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        row_number = 0
        for row in csv_reader:
            if row_number >= 2:
                description = row[1]
                transaction_date = row[2]
                debit = row[3]
                credit = row[4]
                records.append(Record(description, transaction_date, debit, credit, 'EXPENSE'))
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
    read_csv(statement_file)
