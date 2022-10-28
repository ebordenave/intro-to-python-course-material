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


read_last_line('dog_breeds.txt')
