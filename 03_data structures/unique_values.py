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
    print(to_ret)
    return to_ret


d1 = {'G': 3, 'D': 3, 'C': 4, 'Q': 1, 'H': 1, 'M': 2, 'Z': 1, 'W': 3}

unique_values(d1)
