import subprocess
from tkinter import *


def run_code(code_area: Text, output_area: Text):
    code_string = code_area.get('1.0', END)

    try:
        result = subprocess.run()
