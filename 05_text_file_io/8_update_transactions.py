import os
import json


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


sample_transaction_list = [Transaction(**{"id": 10, "type": "debit", "amount": -288.02}),
                           Transaction(**{"id": 88, "type": "debit", "amount": 166.13}),
                           Transaction(**{"id": 502, "type": "credit", "amount": -868.82}),
                           Transaction(**{"id": 683, "type": "debit", "amount": 267.19}),
                           Transaction(**{"id": 683, "type": "debit", "amount": 267.19}),
                           Transaction(**{"id": 772, "type": "credit", "amount": -531.1}),
                           Transaction(**{"id": 772, "type": "credit", "amount": -531.1}),
                           Transaction(**{"id": 930, "type": "credit", "amount": 772.45}),
                           Transaction(**{"id": 930, "type": "credit", "amount": 772.45}),
                           Transaction(**{"id": 979, "type": "debit", "amount": -866.6})]


# receive transactions from both json file and transaction list
def update_transactions(file_path: str, transaction_list):
    # remove duplicate objects from transaction list
    unique_transactions = set(val for val in transaction_list)

    # init new ls
    json_file_ls = []

    # read json file (file_path) and load it
    with open(file_path, 'r') as fp:
        saved_transactions_in_json_file = json.load(fp)

    # remove duplicate transactions from json file and append transactions to new list
    for transaction in saved_transactions_in_json_file:
        if transaction not in json_file_ls:
            json_file_ls.append(transaction)

    # init combined list and assign json file list
    combined_ls = json_file_ls

    # convert transaction objects to python readable list of dictionaries
    for transaction_obj in unique_transactions:
        transaction_dict = transaction_obj.__dict__
        combined_ls.append(transaction_dict)

    print(combined_ls)

    combined_ls = list(
        {
            dictionary['id']: dictionary
            for dictionary in combined_ls
        }.values()
    )

    print(combined_ls)

    with open(file_path, 'w+', encoding='utf-8') as f:
        json.dump(combined_ls, f, ensure_ascii=False, indent=4)

    return None


update_transactions('testing.json', sample_transaction_list)
