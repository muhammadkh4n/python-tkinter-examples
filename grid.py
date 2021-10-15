from tkinter import *

root = Tk()

# Creating label widget
label1 = Label(root, text='Hello World!') #.grid(row=0, column=0)
label2 = Label(root, text='My Name is Khan') #.grid(row=1, column=5)

# putting it on the screen
label1.grid(row=0, column=0)
label2.grid(row=1, column=5)

root.mainloop()
