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
