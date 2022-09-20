# printMathResult.py
# Write a python script that will wait for three user inputted values in the following order:
# a string operation which will be one of the following ('+', '-', '*', '/')
# a number between 1-20
# a number between 1-20
# Once the user inputs the three values, it is supposed to perform the given operation
# (The first inputted value) on the numeric values (The second and third inputted values)
# and print the result to the console. This script should not print any other text to
# the console other than the result of the mathematical operation. Do not print any input prompt.

operator = str(input())
integer_1 = int(input())
integer_2 = int(input())

if operator == '+':
    resultant = integer_1 + integer_2
    print(int(resultant))
elif operator == '-':
    resultant = integer_1 - integer_2
    print(int(resultant))
elif operator == '*':
    resultant = integer_1 * integer_2
    print(int(resultant))
elif operator == '/':
    resultant = integer_1 / integer_2
    print(resultant)
