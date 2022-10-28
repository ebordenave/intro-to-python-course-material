import os


def write_last_line(file_path: str, text: str = ''):
    if text != '' and '\n' not in text[0]:
        # file exists
        # text is not empty
        # if text exists and does not begin with newline
        with open(file_path, 'a') as f:
            f.write('\n' + text)
    elif not text:
        # text is missing or empty
        # file exists
        return 0
    else:
        # file exists
        # text is not empty
        with open(file_path, 'a') as f:
            f.write(text)
    return None


write_last_line('testing.txt')
