# This function will have two parameters. The first is a set of numbers known as Number Set. The second is a dictionary
# known as Dictionary. Dictionary will have keys as integers and values as letters. The functions should return true
# if at least one of the numbers in the Number set is a key in Dictionary. It should return false otherwise.
numberSet = {9, 10, 4}
Dictionary = {5: 'i', 3: 'o', 1: 'N'}


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


dict_contains_keys(numberSet, Dictionary)
