from tkinter import *

# calculate
# render
# draw
# event/input


total = 0


def click():
    global total
    total += 1
    print(f'this button was clicked {total} times')


window = Tk()

window.title("Hello World")
window.geometry("500x300")
label = Label(window, text="Hello Python Developers", font=('Arial Bold', 20))
label.grid(column=0, row=0)
button = Button(window, text="Click Me", command=click)
button.grid(column=4, row=1)
window.mainloop()

# window.button()
