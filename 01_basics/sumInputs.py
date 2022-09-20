# sumInputs.py
# Write a script that accepts an arbitrary number of user inputs. When you receive a user input value that is a number,
# add the number to a growing sum of numbers received as user input. When you receive a user input value that is not a
# number, skip it. When you receive two consecutive user input values that are not numbers, stop accepting user inputs.
# Then Multiply the total number of user inputs received (numbers and non-numbers) times the growing sum of received
# numbers. Finally, print the result to the console as the last line.
# This script should not print any other text to the console other than the result of the mathematical operation.
# Do not print any input prompt.


# init sum
s = 0

# last integer variable
last_integer = None
repeat_counter = 0
# init list
ls = []

nls = []

Num = 0
Sum = 0

while repeat_counter < 2:
    if repeat_counter < 2:
        countable_integer = input()
        if countable_integer.isdigit() is True:
            ls.append(int(countable_integer))
            if repeat_counter > 0:
                repeat_counter -= 1
        if countable_integer.isdigit() is not True:
            nls.append(countable_integer)
            last_integer = countable_integer
            repeat_counter += 1
    Sum = sum(ls)
    Num = len(nls) + len(ls)
print(Num*Sum)
