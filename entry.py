from tkinter import *

root = Tk()

def register():
  name = entry.get()
  label = Label(root, text=name)
  label.pack()

entry = Entry(root, width=50, fg="red", bg="black")
entry.pack()
entry.insert(0, "Enter your name")

button = Button(root, text="Register", command=register)
button.pack()

root.mainloop()
