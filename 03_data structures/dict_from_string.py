# This function will be given a single parameter, a string representing a dictionary. Your job is to convert the
# string into an actual dictionary and return the dictionary. Make sure all key-value pairs in the string exist in
# the newly created dictionary. The string will contain only numbers or single letters as key values pairs. Make sure
# all letters are kept as strings and all numbers are converted to integers in the newly created dictionary.


def dict_from_string(dict_str: str) -> dict:
    res = eval(dict_str)
    print(res)
    return res

# dict_1 = "{9: 'V', 'G': 0, 'M': 9, 'u': 3, 2: 'o', 8: 'u', 'q': 9, 'D': 1}"
# dict_from_string(dict_1)
