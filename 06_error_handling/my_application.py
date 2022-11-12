def remove_duplicates(values: list) -> list:
    new_ls = []

    for val in values:
        if val not in new_ls:
            new_ls.append(val)

    values.clear()
    values.extend(new_ls)

    return values
