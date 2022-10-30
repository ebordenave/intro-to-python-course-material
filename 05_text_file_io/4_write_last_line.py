import os


def write_last_line(file_path: str, text: str = ''):
    if os.stat(file_path).exists:
        if text and '\n' not in text[0]:
            with open(file_path, 'a') as f:
                f.write('\n' + text)
        elif not text:
            return 0
        else:
            with open(file_path, 'a') as f:
                f.write(text)
    else:
        with open(file_path, 'w+') as f:
            f.write('')
    return None


write_last_line('testing.txt')
