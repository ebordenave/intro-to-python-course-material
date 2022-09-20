# sumRange.py
# This script will accept two user inputs that are whole numbers. The first user input will always be less
# than the second input. This script should calculate the sum of every other whole number between the inputs.
# Then print the sum of the numbers to the console.
# This script should not print any other text to the console other than the result of the mathematical operation.
# Do not print any input prompt.


num_1 = int(input())
num_2 = int(input())+1
ls = []
while True:
    if num_1 < num_2:
        for i in range(num_1, num_2, 2):
            ls.append(i)
        Sum = sum(ls)
        print(Sum)
        break
    else:
        break
