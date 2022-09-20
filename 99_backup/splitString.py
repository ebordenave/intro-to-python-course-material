# splitString.py
# Write a script that accepts an arbitrary number of user inputs. Every time this script receives a string,
# it should add the string to a growing string. Newly added strings should be added to the growing string
# at the index equal to the newly added string's length. If the newly added string's length is equal to
# or larger than the growing string, this script should add the new string to the end of the growing string.
# When this script receives a blank input, this application should stop receiving input and print the growing
# string to the console.
# This script should not print any other text to the console other than the result of the growing string.
# Do not print any input prompt.

# user input number of elements
user_input_count = int(input("Enter number of elements: "))

# repeat counter
repeat_counter = 0

while repeat_counter < user_input_count:
    repeat_counter += 1
    user_input_string = input(f"Enter the value of input #{repeat_counter}: ")
    split_string_list = list(user_input_string)
    while repeat_counter < user_input_count:
        repeat_counter += 1
        new_input_string = input(f"Enter the value of input #{repeat_counter}: ")
        x = list(new_input_string)
        split_string_list.insert(len(new_input_string), x)
        flat_list = [item for sublist in split_string_list for item in sublist]
        print(*flat_list, sep="")

# is this for checking if input is space
# for i in ls:
#     try:
#         nls.append(int(i))
#         j = i
#     except ValueError:
#         continue
