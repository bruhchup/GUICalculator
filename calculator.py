from tkinter import *
from tkinter import ttk

root = Tk()

#defines a frame for the Entry
efrm = ttk.Frame(root, padding = 0)
efrm.grid()

#defines a frame for the buttons
frm = ttk.Frame(root, padding = 0)
frm.grid()

#this is the text box
e = Entry(efrm, width = 50, borderwidth= 5)
e.grid(row = 0, column = 0)

'''
The line below disables the ability to input text via the keyboard into the Entry object.
the state is used to disable input, disabledforeground prevents the text from defaulting
to the color gray when disabled
'''
e.config(state='disabled', disabledforeground='black')

def add_button(x):
    '''
    @param x: the character that represents the button
    
    adds the pressed button to the Entry text
    '''
    e.config(state='normal')
    curr = e.get()
    e.delete(0, END)
    e.insert(0, str(curr) + str(x))
    e.config(state='disabled')

def answer():
    '''
    evaluates the string inside the entry widget
    '''
    e.config(state='normal')
    ans = eval(e.get())
    e.delete(0, END)
    e.insert(0, ans)
    e.config(state='disabled')

def clear():
    '''
    clears the Entry text
    '''
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