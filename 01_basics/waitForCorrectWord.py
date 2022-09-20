# waitForCorrectWord.py
# This script should print a single word that it is expecting the user to type in. Then it should wait
# for the user to type the word in. If the user types in a word that does not match the word you
# initially printed, the script should print a single line message saying "the input was incorrect" and
# then wait for the user to try again. The script should repeat this process an indefinite amount of
# times until the user types the correct value.

print("blue")
while True:
    secret_word = "blue"
    user_guess = input()
    if user_guess == secret_word:
        print("That is correct")
        break
    elif user_guess != secret_word:
        print("the input was incorrect")
