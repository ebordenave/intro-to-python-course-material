def flip_matrix(mat: list) -> list:
    result = []
    for i in mat:
        result.insert(0, i)
    # print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in result]))
    return result


def remove_char(str_list: list, char: str) -> list:
    ls = []
    for i in str_list:
        var = i.replace(char, '')
        ls.append(var)
    # print(ls)
    return ls


def return_growing_num_list(max: int) -> list:
    orig_ls = []
    new_ls = []
    for i in range(1, max + 1):
        orig_ls = [i] * i
        string = ' '.join([str(item) for item in orig_ls])
        new_ls.append(string)
    print(new_ls)
    return new_ls


def reverse_number_in_list(number_list: list) -> list:
    rev_list = []
    for i in number_list:
        num = str(i)
        rev_num = num.rstrip('0')
        rev_num = rev_num[::-1]
        rev_list.append(int(rev_num))
    # print(rev_list)
    return rev_list


def tails_same(number_list: list) -> bool:
    first = number_list[0]
    last = number_list[len(number_list) - 1]
    print(first == last)
    return first == last


def dict_contains_keys(items: set, example_dict: dict) -> bool:
    x = 0
    for i in example_dict and items:
        if i in example_dict and items:
            x += 1
        else:
            x += 0
    if x > 0:
        return True
    else:
        return False


def concatenate_dict(dict_list: list) -> dict:
    new_dict = {}
    for sub_dict in dict_list:
        for key, value in sub_dict.items():
            new_dict.setdefault(key, value)
    print(new_dict)
    return new_dict


def unique_values(a_dict: dict) -> dict:
    count = {}
    to_ret = {}
    for v in a_dict.values():
        if v in count:
            count[v] += 1
        else:
            count[v] = 1
    for k, v in count.items():
        if v == 1:
            value = [i for i in a_dict if a_dict[i] == k]
            for elem in value:
                to_ret[k] = elem
    return to_ret


def find_color(colors: set, values: list) -> list:
    ls = []
    for i in values:
        ind_tuple_dict = {i}
        for k, v in ind_tuple_dict:
            if k in colors:
                ls.append(v)
    print(ls)
    return ls


def dict_from_string(dict_str: str) -> dict:
    res = eval(dict_str)
    return res
