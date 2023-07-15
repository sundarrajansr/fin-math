class Record:
    def __init__(self, description, date, debit, credit, record_type):
        self.description = description
        self.date = date
        self.debit = debit
        self.credit = credit
        self.type = record_type