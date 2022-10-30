import os


def delete_last_line(file_path: str) -> str:
    with open(file_path, 'r+') as f:
        if os.stat(file_path).st_size == 0:
            return ''
        else:
            lines = f.readlines()
            last_elem = str(next(reversed(lines.copy())))
            f.seek(0)
            f.truncate()
            f.writelines(lines[:-1])
        print(last_elem)
        return last_elem


delete_last_line('testing.txt')
