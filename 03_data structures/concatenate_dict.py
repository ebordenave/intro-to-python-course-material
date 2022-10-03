dict_list_1 = [{'Z': 6, 'k': 10, 'w': 3, 'I': 8, 'Y': 5}, {'Y': 1, 'Z': 4}, {'X': 2, 'L': 5}]


def concatenate_dict(dict_list: list) -> dict:
    new_dict = {}
    for sub_dict in dict_list:
        for key, value in sub_dict.items():
            new_dict.setdefault(key, value)
    print(new_dict)
    return new_dict


concatenate_dict(dict_list_1)
