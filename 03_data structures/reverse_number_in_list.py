# This function will be given a list of numbers your job is to reverse all the numbers in the list and return a list
# with the reversed numbers. If a number ends with 0 you need to remove all the trailing zeros before reversing the
# number. An example of reversing numbers with trailing zeros:  10 -> 1,  590 -> 95. None of the numbers in the
# number_list will be less than 1.
#
#
# def reverse_number_in_list(number_list:list)-> list:

num_list = []
n = 0
pos = 0

while n < 4:
    num = input()
    rev_num = num.rstrip('0')
    rev_num = rev_num[::-1]
    num_list.append(rev_num)
    print(num_list)
    n += 1

