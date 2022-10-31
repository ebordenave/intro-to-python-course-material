import os
import json
from os import path


# steps below:
# read json file
# convert json file to dictionaries
# read key/value pairs from dictionaries from json file
# keys will ID of transactions
# search or seek keys
# remove duplicate IDs in transaction_list
# new list will remain with unique transaction IDS as keys and type/amount as values
# update/overwrite old list with new list
# write transactions to json file


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


# initialize Transaction objects
Transaction1 = Transaction(96021313, 'debit', 9.25)
Transaction2 = Transaction(96021313, 'credit', 1.25)

# serializes python object to json format
json_string_object = json.dumps(Transaction1.__dict__, indent=4)

# writes transaction object to json file
with open("testing.json", "w") as f:
    f.write(json_string_object)


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
