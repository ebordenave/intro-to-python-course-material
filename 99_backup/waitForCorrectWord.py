# waitForCorrectWord.py
# This script should print a single word that it is expecting the user to type in. Then it should wait
# for the user to type the word in. If the user types in a word that does not match the word you
# initially printed, the script should print a single line message saying "the input was incorrect" and
# then wait for the user to try again. The script should repeat this process an indefinite amount of
# times until the user types the correct value.
string = "secret word"

while string != "blue":
    string = input("The color of the sky during the day is : ")
    if "blue" in string:
        print("That is correct")
    else:
        print("the input was incorrect")
