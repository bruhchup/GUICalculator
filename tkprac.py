from tkinter import *
from tkinter import ttk

root = Tk()

efrm = ttk.Frame(root, padding = 0)
efrm.grid()
frm = ttk.Frame(root, padding = 0)
frm.grid()

e = Entry(efrm, width = 50, borderwidth= 5)
e.grid(row = 0, column = 0)
e.config(state='disabled', disabledforeground='black')

def normal():
    '''
    Changes the state of the Entry to normal. This is so that the input from the buttons can be passed to the Entry.
    When buttons are not being pressed, the state is disabled, which presents users from manually entering characters
    into the entry widget.
    '''
    e.config(state='normal')

def add_button(x):
    '''
    Performs the function of the button pressed
    '''
    e.config(state='normal')
    curr = e.get()
    e.delete(0, END)
    e.insert(0, str(curr) + str(x))
    e.config(state='disabled')
    
def answer():
    '''
    Evaluates the string inside the entry widget
    '''
    e.config(state='normal')
    ans = eval(e.get())
    e.delete(0, END)
    e.insert(0, ans)
    e.config(state='disabled')

def clear():
    e.config(state='normal')
    e.delete(0, END)
    e.config(state='disabled')


def buttons():
    '''
    Layout of calculator buttons
    '''
    one = ttk.Button(frm, text="1", command =lambda: add_button('1')).grid(column=0, row=1)
    two = ttk.Button(frm, text="2", command =lambda: add_button('2')).grid(column=1, row=1)
    three = ttk.Button(frm, text="3", command =lambda: add_button('3')).grid(column=2, row=1)
    four = ttk.Button(frm, text="4", command =lambda: add_button('4')).grid(column=0, row=2)
    five = ttk.Button(frm, text="5", command =lambda: add_button('5')).grid(column=1, row=2)
    six = ttk.Button(frm, text="6", command =lambda: add_button('6')).grid(column=2, row=2)
    seven = ttk.Button(frm, text="7", command =lambda: add_button('7')).grid(column=0, row=3)
    eight = ttk.Button(frm, text="8", command =lambda: add_button('8')).grid(column=1, row=3)
    nine = ttk.Button(frm, text="9", command =lambda: add_button('9')).grid(column=2, row=3)
    zero = ttk.Button(frm, text="0", command =lambda: add_button('0')).grid(column=1, row=4)
    plus = ttk.Button(frm, text="+", command =lambda: add_button('+')).grid(column=3, row=1)
    minus = ttk.Button(frm, text="-", command =lambda: add_button('-')).grid(column=3, row=2)
    mult = ttk.Button(frm, text="*", command =lambda: add_button('*')).grid(column=3, row=3)
    div = ttk.Button(frm, text="/", command =lambda: add_button('/')).grid(column=3, row=4)
    clr = ttk.Button(frm, text="clr", command =lambda: clear()).grid(column=0, row=4)
    equals = ttk.Button(frm, text="=", command =lambda: answer()).grid(column=2, row=4)

    
buttons()


root.mainloop()