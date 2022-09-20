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

# def productSum(x: int, y: int, z: int) -> int
# This function should return:
# The product of x and y, if the product of x and y is less than z.
# Else it should return the sum of x and y, if the product of x and y is greater than or equal to z.


def productSum(x: int, y: int, z: int) -> int:
    if x * y < z:
        product_xy = x * y
        print(product_xy)
    elif x * y >= z:
        sum_xy = x + y
        print(sum_xy)


arg_x = int(input())
arg_y = int(input())
arg_z = int(input())

productSum(arg_x, arg_y, arg_z)
