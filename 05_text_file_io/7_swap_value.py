import os
import json


def swap_value(file_path: str, key: str, replacement):
    with open(file_path, 'r+') as f:
        json_data = json.load(f)
    old_key_value = json_data.get(key)
    json_data[key] = replacement

    with open(file_path, "w") as f:
        json.dump(json_data, f)
    print(old_key_value)
    return old_key_value


swap_value('dict_example.json', 'key_1', 'unhappy lion')
