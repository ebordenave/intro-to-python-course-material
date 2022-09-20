# sumInputs.py
# Write a script that accepts an arbitrary number of user inputs. When you receive a user input value that is a number,
# add the number to a growing sum of numbers received as user input. When you receive a user input value that is not a
# number, skip it. When you receive two consecutive user input values that are not numbers, stop accepting user inputs.
# Then Multiply the total number of user inputs received (numbers and non-numbers) times the growing sum of received
# numbers. Finally, print the result to the console as the last line.
# This script should not print any other text to the console other than the result of the mathematical operation.
# Do not print any input prompt.

# user input number of elements
user_input_count = input("Enter number of elements: ")

# init sum
s = 0

# repeat counter
repeat_counter = 1

# last integer variable
last_integer = None

# init list
ls = []

# init new list
nls = []

while repeat_counter <= int(user_input_count):
    countable_integer = input(f"Enter the value of input #{repeat_counter}: ")
    ls.append(countable_integer)
    # if statement to validate that if the last_integer and countable_integer
    # are equal and countable_integer is zero then break the loop
    if countable_integer.isdigit() is not True and countable_integer == last_integer:
        break
    else:
        last_integer = countable_integer
        repeat_counter += 1
for i in ls:
    try:
        nls.append(int(i))
        j = i
    except ValueError:
        continue
for j in nls:
    s += j
print("sum = ", s)
print("total inputs = ", len(nls))
print(f"{s} * {user_input_count} = {int(user_input_count) * s}")
