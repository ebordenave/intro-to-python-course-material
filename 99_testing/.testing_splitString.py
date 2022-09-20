growing_string = ''

#Input the string.

inputStr = input()


while inputStr != '':
    if len(inputStr) >= len(growing_string):
        growing_string = growing_string + inputStr
    else:
        position = len(inputStr)
        growing_string = growing_string[:position] + inputStr + growing_string[position:]
        inputStr = input()
print(growing_string)
