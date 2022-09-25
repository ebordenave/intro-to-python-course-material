# This function should return true if the value at the beginning and the end of the list are equal. False otherwise.
# Example:
# number_list = [1, 239, 949, 0, 84, 0, 1]
# output: True
# number_list = [1, 239, 949, 0, 84, 0, 13]
# output: False

ls_1 = [1, 239, 949, 0, 84, 0, 1]
ls_2 = [1, 239, 949, 0, 84, 0, 13]


def tails_same(number_list: list) -> bool:
    first = number_list[0]
    last = number_list[len(number_list) - 1]
    print(first == last)
    return first == last


tails_same(ls_2)
