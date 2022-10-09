# You will be given three strings, the first string is a sentence known as text that contains at least one
# occurrence of leftPattern and rightPattern. Left pattern and right pattern are single characters strings
# that you are attempting to remove from the string. Your goal is to remove only the patterns when left
# pattern has an equal number of corresponding right patterns. The patterns are removed in pairs only when
# there is a balanced number of left and right patterns. The patterns may be nested within the text and there
# is no guarantee that a left pattern will occur before the right pattern.


def nestedRemoval(text: str, leftPattern: str, rightPattern: str) -> str:
    while text.count(leftPattern) >= 1 and text.count(rightPattern) >= 1:
        text = text.replace(leftPattern, '', 1).replace(rightPattern, '', 1)
    return text


#
print()
