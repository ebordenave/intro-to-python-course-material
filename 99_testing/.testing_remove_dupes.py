import collections

transaction_list = [1, 2, 3, 2, 1, 5, 6, 5, 5, 5]
dupes = [item for item, count in collections.Counter(transaction_list).items() if count > 1]
transaction_list_no_duplicates = []
print(f"these are the duplicates {dupes}")
seen = set()

for elem in transaction_list:
    if elem not in seen:
        transaction_list_no_duplicates.append(elem)
        seen.add(elem)
transaction_list = list(transaction_list_no_duplicates)
print(f"this is the updated list {transaction_list}")


# print(transaction_list_no_duplicates)