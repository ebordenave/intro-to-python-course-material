import json

# with open('dict_example.json') as file:
#     py_obj = json.load(file)
#     for key, val in py_obj.items():
#         print(key, val)
#
#
# py_obj['key_1'] = "happy lion"
# py_obj['key_2'] = "happy birds"
#
# with open('dict_example.json', 'w') as file:
#     json.dump(py_obj, file, indent=4, sort_keys=True)

with open('data.json', 'w') as json_file:
    json.dump(transaction_list, json_file, indent=4)