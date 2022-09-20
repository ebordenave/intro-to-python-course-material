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

# new list
nls = []


while first_input_string != '':
    ls = list(first_input_string)
    while True:
        second_input_string = str(input())
        if second_input_string != '' and len(second_input_string) < len(ls):
            nls = list(second_input_string)
            ls.insert(len(nls), nls)
        elif second_input_string != '' and len(second_input_string) >= len(ls):
            ls.append(list(second_input_string))
        elif '' == second_input_string:
            break
flat_list = [item for sublist in ls for item in sublist]
print(*flat_list, sep='')
