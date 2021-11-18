from tkinter import *
from typing import Match
from decimal import *

root = Tk()
root.title("Simple Calculator")
root.iconbitmap('.../Calc/favicon.ico')

e = Entry(root, width=40, borderwidth=5)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
e.insert(0, "0")

def button_click(number):
    current = e.get()
    e.delete(0, END)
    print(current)
    #This checks if the number coming in is . and that there is either a 0 or nothing, then add the 0 before
    if number == '.' and (current == '0' or current == None):
        e.insert(0, '0.')
    #if it's just a 0 before this will remove so you won't get a 03 for your number
    elif current == '0':
        e.insert(0, str(number))
    #normal function delete what was in display concatanate the 2 numbers.
    else:
        e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, END)
    e.insert(0, "0")

def button_dot():
    current = e.get()
    #Checks if there is already a decimal in the number if so END and it won't add another
    if '.' in current:
        END
    else:
        button_click('.')

def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = first_number
    e.delete(0,END)
    e.insert(0, "0")

def button_equal():
    second_number = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0, Decimal(f_num) + Decimal(second_number))
    if math == "subtraction":
        e.insert(0, Decimal(f_num) - Decimal(second_number))
    if math == "multiplication":
        e.insert(0, Decimal(f_num) * Decimal(second_number))
    if math == "division":
        e.insert(0, Decimal(f_num) / Decimal(second_number))

def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = first_number
    e.delete(0,END)
    e.insert(0, "0")

def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = (first_number)
    e.delete(0,END)
    e.insert(0, "0")

def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = (first_number)
    e.delete(0,END)
    e.insert(0, "0")

def button_posNeg():
    current = e.get()
    #checks if number is already negative if so removes it
    if '-' in current:
        f_num = current.replace('-', '')
    #if not adds the negative
    else:
        f_num= '-'+current
    e.delete(0, END)
    e.insert(0, str(f_num))


#Define the buttons
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_dot = Button(root, text=".", padx=42, pady=20, command=button_dot)
button_add = Button(root, text="+", padx=39, pady=20, command=button_add)
button_equal = Button(root, text="=", padx=91, pady=20, command=button_equal)
button_clear = Button(root, text="Clear", padx=78, pady=20, command=button_clear)
button_posNeg = Button(root, text="+/-", padx=34, pady=20, command=button_posNeg)
button_subtract = Button(root, text="—", padx=37, pady=20, command=button_subtract)
button_multiply = Button(root, text="X", padx=39, pady=20, command=button_multiply)
button_divide = Button(root, text="/", padx=41, pady=20, command=button_divide)

# Put the buttons on the screen
button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)

button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)

button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)

button_0.grid(row=5, column=0)
button_dot.grid(row=5, column=1)
button_clear.grid(row=1, column=0, columnspan=2)
button_posNeg.grid(row=1, column=2, columnspan=1)
button_add.grid(row=4, column=3)
button_equal.grid(row=5, column=2, columnspan=2)

button_subtract.grid(row=3, column=3)
button_multiply.grid(row=2, column=3)
button_divide.grid(row=1, column=3)

myLabel = Label(root, text="WARNING!!", wraplength=350, foreground="red", font=("Arial", 25)).grid(row=6, column=0, columnspan=4)
myLabel2 = Label(root, text="This is just a test version to show Tkinter and Pyinstaller for Python, this program is for demonstrative purposes only!", wraplength=350, foreground="red").grid(row=7, column=0, columnspan=4)


root.mainloop()