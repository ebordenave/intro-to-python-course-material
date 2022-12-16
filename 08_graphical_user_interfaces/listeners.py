import subprocess
from tkinter import *
import sys
import traceback
import os


def set_text(text_area: Text, text: str):
    text_area.delete('1.0', END)
    text_area.insert(END, text)


def run_code(code_area: Text, output_area: Text):
    code_string = code_area.get('1.0', END)
    py_file_path = 'tmp.py'

    with open(py_file_path, 'w') as f:
        f.write(code_string)

    try:
        result = subprocess.run([sys.executable, py_file_path], stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                encoding='utf-8')

        set_text(output_area, result.stdout)
    except Exception:
        tb = traceback.format_exc()
        set_text(output_area, str(tb))
    finally:
        os.remove(py_file_path)
