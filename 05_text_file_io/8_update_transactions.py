import os
import json
from os import path


# steps below:
# remove duplicates from transaction_list that is received
# read json file
# convert json file to list of dictionaries
# convert transactions objects to dictionaries
# add unique transactions from transaction_list to list of dictionaries
# do not add duplicates
# update/overwrite old list with new list
# write transactions_list to json file


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
# json_string_object = json.dumps(Transaction1.__dict__, indent=4)
# json_string_object2 = json.dumps(Transaction2.__dict__, indent=4)


# with open("testing.json", "w") as f:
#     f.write(json_string_object2)
#     f.write(json_string_object)


def update_transactions(file_path: str, transaction_list: list):
    transaction_list_no_duplicates = []

# remove duplicate transactions from transactions_list
    for transaction in transaction_list:
        if transaction not in set():
            transaction_list_no_duplicates.append(transaction)
            set().add(transaction)
    transaction_list = list(transaction_list_no_duplicates)
    print(transaction_list)

# open and read json file / deserialize transaction data into list of dictionaries
    with open(file_path, 'r') as json_file:
        transaction_data_ls = [json.load(json_file)]
        print(type(transaction_data_ls))
