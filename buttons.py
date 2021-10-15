import builtins
from tkinter import *

root = Tk()

def buttonClick():
  label = Label(root, text='Kaboom!')
  label.grid(row=0, column=1)

button = Button(root, text='Click Me!', command=buttonClick, fg="blue", bg="#fff")

button.grid(row=0, column=0)

root.mainloop()
