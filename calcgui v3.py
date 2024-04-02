#calculator built with my own UI
#memory save fuction requested with external file save
#additioanlly from last time M+, MRC, and MC buttons to be added
#byrequest


# Things to do
# Remove braces from sum
# Colourise the background
# Add an LCD looking screen
# Change font for sum and answer



#import modules
import os
from tkinter import *
 
#create root window
root = Tk()
 
#root window title and dimension
root.title("Calculator!")
#set geometry (widthxheight)
root.geometry('322x200')

#set up variables for application
number_selection = 1
operator_selection = ""
entery_1 = []
entery_2 = []
number_1 = 0
number_2 = 0
answer = 0

#function button click actions
def add():
    global number_1
    number_1 = ''.join(entery_1)
    global operator_selection
    operator_selection = "+"
    global number_selection
    number_selection = 2
    sumtext = str(number_1) + " ", operator_selection
    lblsum.configure(text= sumtext)
    print('add things')
def subtract():
    global number_1
    number_1 = ''.join(entery_1)
    global operator_selection
    operator_selection = "-"
    global number_selection
    number_selection = 2
    sumtext = str(number_1) + " ", operator_selection
    lblsum.configure(text= sumtext)
    print('subtract things!')
def multiply():
    global number_1
    number_1 = ''.join(entery_1)
    global operator_selection
    operator_selection = "*"
    global number_selection
    number_selection = 2
    sumtext = str(number_1) + " ", operator_selection
    lblsum.configure(text= sumtext)
    print('multiply things')
def divide():
    global number_1
    number_1 = ''.join(entery_1)
    global operator_selection
    operator_selection = "/"
    global number_selection
    number_selection = 2
    sumtext = str(number_1) + " ", operator_selection
    lblsum.configure(text= sumtext)
    print('divide things!')
def ac():
    global number_selection
    global operator_selection
    global entery_1
    global entery_2
    global number_1
    global number_2
    global answer

    number_selection = 1
    operator_selection = ""
    entery_1 = []
    entery_2 = []
    number_1 = 0
    number_2 = 0
    answer = 0
    lblsum.configure(text= "")
    lblans.configure(text=answer)
def equals():
    global number_2
    number_2 = ''.join(entery_2)

    print(number_1)
    print(number_2)

    if operator_selection == "+":
        print("adding!")
        global answer
        answer = int(number_1) + int(number_2)
        sumtext = number_1 + ' ' + operator_selection + ' ' + number_2 + ' ' + '='
        lblsum.configure(text= sumtext)
        lblans.configure(text = answer)
        print(answer)
    elif operator_selection == "-":
        print("subtracting!")
        #global answer
        answer = int(number_1) - int(number_2)
        sumtext = number_1 + ' ' + operator_selection + ' ' + number_2 + ' ' + '='
        lblsum.configure(text= sumtext)
        lblans.configure(text = answer)
        print(answer)
    elif operator_selection == "*":
        print("multiplying!")
        #global answer
        answer = int(number_1) * int(number_2)
        sumtext = number_1 + ' ' + operator_selection + ' ' + number_2 + ' ' + '='
        lblsum.configure(text= sumtext)
        lblans.configure(text = answer)
        print(answer)
    elif operator_selection == "/":
        print("dividing!")
        #global answer
        answer = int(number_1) / int(number_2)
        sumtext = number_1 + ' ' + operator_selection + ' ' + number_2 + ' ' + '='
        lblsum.configure(text= sumtext)
        lblans.configure(text = answer)
        print(answer)
    else:
        print("no work :(")
def memplus():
    if entery_2 == []:
        f = open("memory.txt", "w")
        number_1 = ''.join(entery_1)
        f.write(number_1)
        f.close()
        print('write number 1 to a file!')
    else:
        f = open("memory.txt", "w")
        f.write(str(answer))
        f.close()
        print('write answer to a file!')
def memclear():
    os.remove("memory.txt")
    print("clear the memory file")
def memrecall():
    global entery_1
    global entery_2
    if len(entery_1) != 0:
        print("entery 1 not empty")
        with open('memory.txt', 'r') as file:
            entery_2 = file.read().rstrip()
            print(entery_2)
    else:
        print("entery 1 empty")
        with open('memory.txt', 'r') as file:
            entery_1 = file.read().rstrip()
            print(entery_1)
    print("recall the memory")
#number button click actions
def one():
    if number_selection == 1:
        entery_1.append("1")
    else:
        entery_2.append("1")

    print("one")
def two():
    if number_selection == 1:
        entery_1.append("2")
    else:
        entery_2.append("2")
    print("two")
def three():
    if number_selection == 1:
        entery_1.append("3")
    else:
        entery_2.append("3")
    print("three")
def four():
    if number_selection == 1:
        entery_1.append("4")
    else:
        entery_2.append("4")

    print("four")
def five():
    if number_selection == 1:
        entery_1.append("5")
    else:
        entery_2.append("5")
    print("five")
def six():
    if number_selection == 1:
        entery_1.append("6")
    else:
        entery_2.append("6")
    print("six")
def seven():
    if number_selection == 1:
        entery_1.append("7")
    else:
        entery_2.append("7")

    print("seven")
def eight():
    if number_selection == 1:
        entery_1.append("8")
    else:
        entery_2.append("8")
    print("eight")
def nine():
    if number_selection == 1:
        entery_1.append("9")
    else:
        entery_2.append("9")
    print("nine")
def zero():
    if number_selection == 1:
        entery_1.append("0")
    else:
        entery_2.append("0")
    print("zero")

#building up the different components
#labels
lbl = Label(root, text = "Calculator!")
lblsum = Label(root, text = "")
lblans = Label(root, text = answer)
#numberbuttons
btn_one = Button(root, text = "1", fg = "red", command=one)
btn_two = Button(root, text = "2", fg = "red", command=two)
btn_three = Button(root, text = "3", fg = "red", command=three)
btn_four = Button(root, text = "4", fg = "red", command=four)
btn_five = Button(root, text = "5", fg = "red", command=five)
btn_six = Button(root, text = "6", fg = "red", command=six)
btn_seven = Button(root, text = "7", fg = "red", command=seven)
btn_eight = Button(root, text = "8", fg = "red", command=eight)
btn_nine = Button(root, text = "9", fg = "red", command=nine)
btn_zero = Button(root, text = "0", fg = "red", command=zero)
#function buttons
btn_add = Button(root, text = "+", fg = "red", command=add)
btn_sub = Button(root, text = "-", fg = "red", command=subtract)
btn_mul = Button(root, text = "*", fg = "red", command=multiply)
btn_div = Button(root, text = "/", fg = "red", command=divide)
btn_equals = Button(root, text = "=", fg = "red", command=equals)
btn_mem_plus = Button(root, text = "M+", fg = "red", command=memplus)
btn_mem_recall = Button(root, text = "MRC", fg = "red", command=memrecall)
btn_mem_clear = Button(root, text = "MC", fg = "red", command=memclear)
btn_ac =Button(root, text = "AC", fg = "red", command=ac)

#structure of application
#set up labels
lbl.grid(column=2, row=0)
lblsum.grid(column=2, row=1)
lblans.grid(column=2, row=2)
#function buttons
btn_add.grid(column=4, row=4)
btn_sub.grid(column=4, row=5)
btn_mul.grid(column=4, row=6)
btn_div.grid(column=4, row=7)
btn_equals.grid(column=5, row=7)
btn_mem_plus.grid(column=5, row=4)
btn_mem_recall.grid(column=5, row=5)
btn_mem_clear.grid(column=5, row=6)
btn_ac.grid(column=0 , row=7)
#number buttons
btn_one.grid(column=0, row=4)
btn_two.grid(column=1, row=4)
btn_three.grid(column=2, row=4)
btn_four.grid(column=0, row=5)
btn_five.grid(column=1, row=5)
btn_six.grid(column=2, row=5)
btn_seven.grid(column=0, row=6)
btn_eight.grid(column=1, row=6)
btn_nine.grid(column=2, row=6)
btn_zero.grid(column=1, row=7)

#execute tkinter
root.mainloop()