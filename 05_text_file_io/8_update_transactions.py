import os
import json
from os import path


class Transaction:

    def __init__(self, id: int, type: str, amount: float):
        self.id: int = id
        self.type: str = type
        self.amount: float = amount

    def __str__(self):
        return f'Transaction[{self.id}] {self.type} ${self.amount}'

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        return hasattr(other, 'id') and other.id == self.id


# initialize Transaction object
Transaction1 = Transaction(96021313, 'debit', 9.25)
Transaction2 = Transaction(96021313, 'credit', 1.25)

print(json.dumps(Transaction1, default=lambda o: o.__dict__, sort_keys=True, indent=4))

# print(vars(Transaction1))
# print(Transaction1)


# convert to JSON dictionary, note id will be key, type and amount will be value?
# with open('testing_json.txt', 'w') as f:
#     json.dump([Transaction1.__dict__ for Transaction1 in new_ls], f)

# def update_transactions(file_path: str, transaction_list: list):
#     seen = set()
#     transaction_list_no_duplicates = []
#
#     for transaction in transaction_list:
#         if transaction not in seen:
#             transaction_list_no_duplicates.append(transaction)
#             seen.add(transaction)
#     transaction_list = list(transaction_list_no_duplicates)
#     print(transaction_list)
#
#     with open(file_path, 'w+') as f:
#         json.dump('some text', f)
#
#     return None
