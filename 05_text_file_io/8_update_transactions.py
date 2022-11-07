import os
import json
from os import path


# def update_transactions(file_path: str, transaction_list: list):
#     """
#     You are part of a team tasked to create an application that helps bankers by saving their transactions for them.
#     Your job within the project is to implement the feature that actually saves the transactions to the hard drive.
#     The scope of your task is that you will be given a file path to where the data should be written and a list of
#     bank transaction objects to be written to the file. The file will contain a JSON array of transactions that the
#     banker previously saved. The bankers at this bank are silly sometimes and they make duplicate transactions, your
#     function should remove the duplicate transactions in the transaction_list and update the existing transaction list
#     saved in the file with the new transactions. Make sure when you are preforming the update of the new transactions
#     that you overwrite old transactions (transactions that already exist in the file) with duplicate new transactions
#     (transactions that are found in the transaction_list). You will know that a transaction is a duplicate if it has
#      the same ID.
#
#     In the end the file should contain a JSON list with transaction Objects that have been updated with the new
#     information from the transaction_list. The JSON list should contain no transactions with the same ID.
#
#     The transaction object referred to here in is outlined below. In actual testing of your code the professors
#     transaction object will be used, which will have all the documented functionality.
#
#     class Transaction:
#
#         def __init__(self, id:int, type:str, amount:float):
#             self.id:int = id
#             self.type:str = type
#             self.amount:float = amount
#
#         def __str__(self):
#             return f'Transaction[{self.id}] {self.type} ${self.amount}'
#
#         def __hash__(self):
#             return hash(self.id)
#
#         def __eq__(self, other):
#             return hasattr(other,'id') and other.id == self.id
#
#     :param file_path: A path to file blank file that holds a JSON list of existing transaction and where the new
#      transaction data should be written
#     :param transaction_list: A list of transaction
#     :return: None
#     """


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

    # init combined the lists into one list
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
