#calculator built to the following spec: Create a simple prototype 
#GUI version of your calculator program. This is likely to have 
#two textboxes in which to enter two numeric values, four buttons 
#(one for each of the basic arithmetic calculations  =, -, *, /) 
#and will display the calculation answer in a label.

# Import Module
from tkinter import *
 
# create root window
root = Tk()
 
# root window title and dimension
root.title("Calculator!")
# Set geometry (widthxheight)
root.geometry('375x135')

#button click actions

def add():
    number_1 = float(txt_1.get())
    number_2 = float(txt_2.get())
    lblans.configure(text = number_1 + number_2)

def subtract():
    number_1 = float(txt_1.get())
    number_2 = float(txt_2.get())
    lblans.configure(text = number_1 - number_2)

def multiply():
    number_1 = float(txt_1.get())
    number_2 = float(txt_2.get())
    lblans.configure(text = number_1 * number_2)

def divide():
    number_1 = float(txt_1.get())
    number_2 = float(txt_2.get())
    lblans.configure(text = number_1 / number_2)

#setting up the different components
lbl = Label(root, text = "Calculator!")
lbl1 = Label(root, text = "Please enter the two values, then select the operator!")
#text entery boxes
txt_1 = Entry(root, width=10)
txt_2 = Entry(root, width=10)
#calculator buttons
btn_add = Button(root, text = "+", fg = "red", command=add)
btn_sub = Button(root, text = "-", fg = "red", command=subtract)
btn_mul = Button(root, text = "*", fg = "red", command=multiply)
btn_div = Button(root, text = "/", fg = "red", command=divide)
lblans = Label(root, text = "Answer will be here")


#set up calculator buttons and text entery boxes, the strucutre
lbl.grid(column=0, row=0)
lbl1.grid(column=0, row=1)
txt_1.grid(column =0, row =2)
txt_2.grid(column =0, row =3)
btn_add.grid(column=1, row=0)
btn_sub.grid(column=1, row=1)
btn_mul.grid(column=1, row=2)
btn_div.grid(column=1, row=3)
lblans.grid(column=0, row=4)

 

#execute tkinter
root.mainloop()