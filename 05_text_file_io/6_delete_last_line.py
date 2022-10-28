def delete_last_line(file_path: str) -> str:
    # """
    # Removes the last line in the file at the specified file path. Then it saves the new value with the last line
    # removed to the file. Finally it returns the deleted last line. If the file has nothing in it an empty
    # string ("") is returned.
    # :param file_path: A path to file
    # :return: The text in the file with the last line removed