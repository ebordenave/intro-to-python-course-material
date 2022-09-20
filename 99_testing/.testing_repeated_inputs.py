amount_of_integers = int(input("How many numbers do you want to count together: "))
s = 0
repeat_counter = 1
# last integer variable
last_integer = None

while repeat_counter <= amount_of_integers:
    countable_integer = int(input(f"Enter the value of the number {repeat_counter}: "))
    # if statement to validate that if the last_integer and countable_integer
    # are equal and countable_integer is zero then break the loop
    if countable_integer == last_integer:
        break
    else:
        last_integer = countable_integer
    s += countable_integer
    repeat_counter += 1

print()
print("The sum of counted numbers is", s)
