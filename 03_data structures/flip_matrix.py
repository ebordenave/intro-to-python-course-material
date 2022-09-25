# flip_matrix(mat:list)->list You will be given a single parameter a 2D list (A list with lists within it) this will
# look like a 2D matrix when printed out, see examples below. Your job is to flip the matrix on its horizontal axis.
# In other words, flip the matrix horizontally so that the bottom is at top and the top is at the bottom. Return the
# flipped matrix.
#
# To print the matrix to the console:
#
#  print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in mat]))
# Example:
#
# Matrix:
# W R I T X
# H D R L G
# L K F M V
# G I S T C
# W N M N F
# Expected:
# W N M N F
# G I S T C
# L K F M V
# H D R L G
# W R I T X


result = []

list = [[72, 85, 87, 90, 69], [80, 87, 65, 89, 85], [96, 91, 70, 78, 97], [90, 93, 91, 90, 94], [57, 89, 82, 69, 60]]


def flip_matrix(mat: list) -> list:
    for i in mat:
        result.insert(0, i)
    for i in result:
        for j in i:
            print(j, end=" ")
        print()


flip_matrix(list)
