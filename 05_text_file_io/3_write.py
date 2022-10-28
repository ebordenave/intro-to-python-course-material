import os


def write(file_path: str, text: str = ''):
    if not text:
        with open(file_path, 'w') as f:
            f.write('')
    else:
        with open(file_path, 'w') as f:
            f.write(text)
    return None


write('dog_breeds.txt')
