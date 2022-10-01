# remove_char(str_list:list, char:str) -> list This function will be given a list of strings and a character. You
# must remove all occurrences of the character from each string in the list. The function should return the list of
# strings with the character removed.
# Example:
# str_list = ['adndj', 'adjdlaa', 'aa', 'djoe']
# char: a
#
# output = ['dndj', 'djdl', '', 'djoe']


def remove_char(str_list: list, char: str) -> list:
    ls = []
    for i in str_list:
        var = i.replace(char, '')
        ls.append(var)
    return ls


list_1 = ['adndj', 'adjdlaa', 'aa', 'djoe']

remove_char(list_1, 'a')
