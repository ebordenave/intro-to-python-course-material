# numberGuess.py
# You will create a script that allows a user to guess a hardcoded number you have picked. If the user's input is
# too high, you should print a message saying "the guess is too high", if the number is too low, you should print
# a message saying "the guess is too low". The first user input this script receives is going to be the total
# number of guesses that the user will have. All subsequent inputs will be guesses. If the user guesses the correct
# value print "correct" and the application should quit. If the user fails to guess the correct value within the
# specified number of guesses print, "you lose" then quit.
#
# Programmatic Description:
# Pick a number between 1 and 10 hard code it in this script. Accept a user input, which will be a number;
# this inputted value is going to be the total number of attempts the user will have to guess the number.
# This number will be greater than zero. Then allow the user to guess the specified total number of times.
# If the guess is too high print, "the guess is too high" if the guess is too low print, "the guess is too low".
# If the user correctly guesses the number in the allotted number of guesses print "correct" then immediately quit.
# And if they fail to guess the correct number print, "you lose" then immediately quit.
# This script should not print any other text to the console other than the outputs outlined above.
# Do not print any input prompt.

import random
# testing
# user input number of elements
max_number_guesses = int(input())

guess_count = 0

secret_guess_number = random.randint(1, 10)

while guess_count <= max_number_guesses:
    user_guess_input = int(input())
    guess_count += 1
    if user_guess_input > secret_guess_number and guess_count < max_number_guesses:
        print("the guess is too high")
    elif user_guess_input < secret_guess_number and guess_count < max_number_guesses:
        print(f"the guess is too low")
    elif user_guess_input == secret_guess_number and guess_count <= max_number_guesses:
        print("correct")
        break
    elif user_guess_input != secret_guess_number and guess_count == max_number_guesses:
        print(f"you lose")
        break
