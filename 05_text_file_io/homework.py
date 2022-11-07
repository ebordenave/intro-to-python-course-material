import os
import json


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
    if os.path.exists(file_path):
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


def clear(file_path: str):
    open(file_path, 'w').close()
    return None


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


def swap_value(file_path: str, key: str, replacement):
    with open(file_path, 'r') as f:
        json_data = json.load(f)
    old_key_value = json_data.get(key)
    json_data[key] = replacement

    with open(file_path, "w") as f:
        json.dump(json_data, f)
    print(old_key_value)
    return old_key_value


def update_transactions(file_path: str, transaction_list):
    unique_transactions = set(val for val in transaction_list)
    json_file_ls = []
    with open(file_path, 'r') as fp:
        saved_transactions_in_json_file = json.load(fp)
    for transaction in saved_transactions_in_json_file:
        if transaction not in json_file_ls:
            json_file_ls.append(transaction)
    combined_ls = json_file_ls
    for transaction_obj in unique_transactions:
        transaction_dict = transaction_obj.__dict__
        combined_ls.append(transaction_dict)
    print(combined_ls)
    combined_ls = list(
        {
            dictionary['id']: dictionary
            for dictionary in combined_ls
        }.values()
    )
    print(combined_ls)
    with open(file_path, 'w+', encoding='utf-8') as f:
        json.dump(combined_ls, f, ensure_ascii=False, indent=4)
    return None
