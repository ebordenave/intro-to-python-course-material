def find_color(colors: set, values: list) -> list:
    ls = []
    for i in values:
        ind_tuple_dict = {i}
        for k, v in ind_tuple_dict:
            if k in colors:
                ls.append(v)
    print(ls)
    return ls
