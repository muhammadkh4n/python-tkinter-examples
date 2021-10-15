from tkinter import *

root = Tk()

root.title('Simple Calc')

input = Entry(root, width=35, borderwidth=5)
input.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def button_click(value):
  if value is 'Clear':
    input.delete(0, END)
    return
  current = input.get()
  input.delete(0, END)
  input.insert(0, str(current) + str(value))

def create_button(text, row, column, padx=40, columnspan=1, command=button_click):
  button = Button(root, text=text, padx=padx, pady=20, command=lambda: command(text))
  button.grid(row=row, column=column, columnspan=columnspan)

button7 = create_button('7', 1, 0)
button8 = create_button('8', 1, 1)
button9 = create_button('9', 1, 2)

button4 = create_button('4', 2, 0)
button5 = create_button('5', 2, 1)
button6 = create_button('6', 2, 2)

button1 = create_button('1', 3, 0)
button2 = create_button('2', 3, 1)
button3 = create_button('3', 3, 2)

button0 = create_button('0', 4, 0)
button_clear = create_button('Clear', 4, 1, 90, 2)

button_plus = create_button('+', 5, 0, 39)
button_equals = create_button('=', 5, 1, 101, 2)

root.mainloop()
