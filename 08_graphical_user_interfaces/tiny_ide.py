from tkinter import *
from turtle import width

window = Tk()

window.title('t.IDE')
window.minsize(width=200, height=200)

code_label = Label(window, text="Code", font=('Arial Bold', 10))
code_area = Text(window, height=15, font=('Courier', 10))


# layout
code_label.grid(column=0, row=0, sticky='w')
code_area.grid(column=0, row=1, sticky='w')
code_scroll = Scrollbar(window, command=code_area.yview)

# output
output_label = Label(window, text="Terminal", font=('Arial Bold', 10))
output_area = Text(window, height=15, font=('Courier', 10))
output_scroll = Scrollbar(window, command=code_area.yview)

output_label.grid(column=0, row=2, sticky='w')
output_area.grid(column=0, row=3, sticky='w')
output_scroll.grid(column=7, row=4, sticky='nesw')



# code_label.grid(column=0,row=0, sticky='w')
# code_area.grid(column=0,row=1, sticky='w')
# code_scroll.grid(column=7, row=1, sticky='nesw')


window.mainloop()
