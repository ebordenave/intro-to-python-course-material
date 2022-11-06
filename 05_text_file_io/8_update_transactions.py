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


sample_transaction_list = [Transaction(**{'id': 22961313, 'type': 'withdrawal', 'amount': 12.5}),
                           Transaction(**{'id': 22961313, 'type': 'deposit', 'amount': 1002.25}),
                           Transaction(**{'id': 44556677, 'type': 'charge', 'amount': 159.99})]


def update_transactions(file_path: str, transaction_list: list):
    unique_transactions = set(val for val in transaction_list)
    print(f"1 unique transactions - {unique_transactions}")

    with open(file_path, 'r') as fp:
        saved_transactions = json.load(fp)
    print(f"2 saved transactions - {saved_transactions}")

    new_ls = []

    for transaction_dict in saved_transactions:
        transaction_object = Transaction(**transaction_dict)
        json_object = json.dumps(transaction_object.__dict__)
        new_ls.append(json_object)
        print(f"3 - {new_ls}")

    # with open(file_path, 'w+', encoding='utf-8') as fp:
    #     json.dump(new_ls, fp, ensure_ascii=False, sort_keys=True, indent=4)
    return None


update_transactions('testing.json', sample_transaction_list)
