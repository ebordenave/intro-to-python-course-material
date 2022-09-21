# splitString.py
# Write a script that accepts an arbitrary number of user inputs. Every time this script receives a string,
# it should add the string to a growing string. Newly added strings should be added to the growing string
# at the index equal to the newly added string's length. If the newly added string's length is equal to
# or larger than the growing string, this script should add the new string to the end of the growing string.
# When this script receives a blank input, this application should stop receiving input and print the growing
# string to the console.
# This script should not print any other text to the console other than the result of the growing string.
# Do not print any input prompt.

# list
ls = []

first_input_string = str(input())

growing_string = ''

# new list
nls = []

while first_input_string != '':
    if len(first_input_string) >= len(growing_string):
        growing_string = growing_string + first_input_string
    else:
        pos = len(first_input_string)
        growing_string = growing_string[:pos] + first_input_string + growing_string[pos:]
        first_input_string = str(input())
print(growing_string)
