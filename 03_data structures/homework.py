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
    for i in range(max + 1):
        orig_ls = [i] * i
        for _ in orig_ls:
            new_ls.append(str(i))
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
        print(x)
        return True
    else:
        print(x)
        return False
