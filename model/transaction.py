
'''

Transaction type holds the following state

narration - string
card type -
amount


'''



class Transaction:
    def __init__(self, narration : str, type : str, debit: bool, amount : float):
        self.type = type
        self.debit = debit
        self.mode = narration.split('-')[0]

    def __str__(self):
        return