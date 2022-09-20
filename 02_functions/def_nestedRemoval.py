# You will be given three strings, the first string is a sentence known as text that contains at least one
# occurrence of leftPattern and rightPattern. Left pattern and right pattern are single characters strings
# that you are attempting to remove from the string. Your goal is to remove only the patterns when left
# pattern has an equal number of corresponding right patterns. The patterns are removed in pairs only when
# there is a balanced number of left and right patterns. The patterns may be nested within the text and there
# is no guarantee that a left pattern will occur before the right pattern.


def nestedRemoval(text: str, leftPattern: str, rightPattern: str) -> str:
    # List to store indices to be removed
    removed_list = []
    # Temporarily store indices
    temp_list = []
    for i in range(len(text)):
        s = text[i]
        if s is leftPattern:
            temp_list.append(i)
        elif s is rightPattern:
            if len(temp_list) > 0 and text[temp_list[-1]] is leftPattern:
                removed_list.append(temp_list[-1])
                removed_list.append(i)
                temp_list = temp_list[:-1]
            else:
                temp_list.append(i)
    ans = ''
    for i in range(len(text)):
        if i not in removed_list:
            ans = ans + text[i]

    return ans

# test
if __name__ == '__main__':
    text = "{{Muscat}} {}mecum tollgate} poultry quarrymen pantheon asteria"
    leftPattern = "{"
    rightPattern = "}"
print('text = ', text)
print('leftPattern = ', leftPattern)
print('rightPattern = ', rightPattern)
print('return = ', nestedRemoval(text, leftPattern, rightPattern))
print()
text = "theretofore [][] demography]] pirouetting morsel [[pesticide"
leftPattern = "["
rightPattern = "]"
print('text = ', text)
print('leftPattern = ', leftPattern)
print('rightPattern = ', rightPattern)
print('return = ', nestedRemoval(text, leftPattern, rightPattern))

#
# print(nestedRemoval(str(input()), str(input()), 'y'))
