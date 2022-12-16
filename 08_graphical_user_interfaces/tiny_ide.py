from msilib.schema import ListBox
from tkinter import *
from turtle import width
import listeners
import os

window = Tk()
current_dir = os.getcwd()

window.title('t.IDE')
window.minsize(width=200, height=200)

# code
code_label = Label(window, text="Code:", font=('Arial Bold', 10))
code_area = Text(window, height=15, font=('Courier', 10))
code_scroll = Scrollbar(window, command=code_area.yview)
code_area['yscrollcommand'] = code_scroll.set

# output
output_label = Label(window, text="Terminal", font=('Arial Bold', 10))
output_area = Text(window, height=15, font=('Courier', 10))
output_scroll = Scrollbar(window, command=code_area.yview)
output_area['yscrollcommand'] = output_scroll.set

# button
save_btn = Button(window, text="Save")
run_btn = Button(window, text="Run", command=lambda: listeners.run_code(code_area, output_area))
exit_btn = Button(window, text="Exit")
dir_btn = Button(window, text="Directory")

# Files
files = StringVar(value=os.listdir(current_dir))

# file_list_box = ListBox(window, listvariable=files, height=5, selectmode='single')
# file_scroll = Scrollbar(window, orient='vertical', command=file_list_box.yview)
# file_list_box['yscrollcommand'] = file_scroll.set



# layout
code_label.grid(column=2, row=0, sticky='w')
code_area.grid(column=2, row=1, sticky='w')
code_scroll.grid(column=5, row=1, sticky='nsew')


output_label.grid(column=2, row=5, sticky='w')
output_area.grid(column=2, row=6, columnspan=5, rowspan=4)
output_scroll.grid(column=5, row=6, columnspan=1, rowspan=4, sticky='nesw')

run_btn.grid(column=4, row=0, sticky='e')
run_btn.grid(column=2, row=6, sticky='e')
run_btn.grid(column=5, row=6, sticky='e')

# code_label.grid(column=0,row=0, sticky='w')
# code_area.grid(column=0,row=1, sticky='w')
# code_scroll.grid(column=7, row=1, sticky='nesw')


window.mainloop()
