# return_growing_num_list(max:int) -> list This function will be given a single number, it should return a list of
# strings of numbers. Each string in the list will only contain a single number repeated an arbitrary amount of
# times. The number each string will contain will be equal to the current string's index+1. The number in the string
# should be repeated the same number of times as the string's index+1. Each number in the string should be separated
# by a space. This list should stop when its size equals the max number specified.
#
# Example:
#
# max = 3
#
# output = ['1', '2 2', '3 3 3']
#
# max = 4
#
# output = ['1', '2 2', '3 3 3', '4 4 4 4']
#
ls = []
nls = []


def return_growing_num_list(max: int) -> list:
    max = range(int(input()) + 1)
    for i in max:
        ls = [i] * i
        for _ in ls:
            nls.append(i)
    print(nls)
    return nls


return_growing_num_list(max)
