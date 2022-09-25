# def productSum(x: int, y: int, z: int) -> int
# This function should return:
# The product of x and y, if the product of x and y is less than z.
# Else it should return the sum of x and y, if the product of x and y is greater than or equal to z.
# Example 1:
# x = 5
# y = 2
# z = 9
# output = 7 = 5 + 2 because 5 * 2 > 9
# Example 2:
# x = 4
# y = 3
# z = 19
# output = 12 = 4 * 3 because 4 * 3 < 19
from _distutils_hack import override


# def productSum(x: int, y: int, z: int) -> int
# This function should return:
# The product of x and y, if the product of x and y is less than z.
# Else it should return the sum of x and y, if the product of x and y is greater than or equal to z.


def productSum(x: int, y: int, z: int) -> int:
    if x * y < z:
        # if the product of x times y is less than the value of z
        product_xy = x * y
        # assign the product value to the variable named product_xy
        print(product_xy)
        return product_xy
    elif x * y >= z:
        # if x times y is greater than the value of z
        sum_xy = x + y
        # assign the sum of x + y to the sum_xy variable
        print(sum_xy)
        return sum_xy


productSum(x=2, y=4, z=32)
