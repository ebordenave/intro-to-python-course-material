import os


def read(file_path: str) -> str:
    if os.stat(file_path).st_size == 0:
        return ''
    else:
        with open(file_path, 'r') as f:
            read_data = f.read()
        # print(read_data)
        return read_data
