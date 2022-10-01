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
    # For each element in x range, x is the length of the text do the following
    for i in range(len(text)):
        # initialize var s and assign the value of the text string at the index
        s = text[i]
        if s is leftPattern:
            # if s is equal to the leftPattern, append element to temporary list
            temp_list.append(i)
        elif s is rightPattern:
            # if s is equal to the rightPattern
            if len(temp_list) > 0 and text[temp_list[-1]] is leftPattern:
                # if the length of the temporary list is greater than 0 and the index of the temp list minus 1 is
                # equal to the left pattern
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

#
print()
