import os


def read_last_line(file_path: str) -> str:
    if os.stat(file_path).st_size == 0:
        # print('')
        return ''
    else:
        with open(file_path, 'r') as f:
            last_line = f.readlines()[-1]
            # print(last_line)
        return last_line


def read(file_path: str) -> str:
    if os.stat(file_path).st_size == 0:
        return ''
    else:
        with open(file_path, 'r') as f:
            read_data = f.read()
        # print(read_data)
        return read_data


# line parameter might be called text, check the unit test
def write(file_path: str, text: str = ''):
    if not text:
        with open(file_path, 'w') as f:
            f.write('')
    else:
        with open(file_path, 'w') as f:
            f.write(text)
    return None


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
