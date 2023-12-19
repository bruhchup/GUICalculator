from tkinter import *
from tkinter import ttk
from customtkinter import *

root = CTk()

ttk.Style().theme_use('clam')

#defines a frame for the Entry
efrm = ttk.Frame(root, padding = 0)
efrm.grid()

#defines a frame for the buttons
frm = ttk.Frame(root, padding = 0)
frm.grid()

#this is the text box
e = Entry(efrm, width = 17, borderwidth= 2, font = 'Arial 32')
e.grid(row = 0, column = 0)
e.pack()

'''
The line below disables the ability to input text via the keyboard into the Entry object.
the state is used to disable input, disabledforeground prevents the text from defaulting
to the color gray when disabled
'''
e.config(state='disabled', disabledforeground='black', disabledbackground='white')

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
    try: 
        ans = eval(e.get())
    except:
        e.config(state='disabled')
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
    one = Button(frm, text="1", height = 2, width = 5, font = 'Arial 24',command =lambda: add_button('1')).grid(column=0, row=3)
    two = Button(frm, text="2", height = 2, width = 5, font = 'Arial 24', command =lambda: add_button('2')).grid(column=1, row=3)
    three = Button(frm, text="3", height = 2, width = 5, font = 'Arial 24', command =lambda: add_button('3')).grid(column=2, row=3)
    four = Button(frm, text="4", height = 2, width = 5, font = 'Arial 24', command =lambda: add_button('4')).grid(column=0, row=2)
    five = Button(frm, text="2", height = 2, width = 5, font = 'Arial 24', command =lambda: add_button('2')).grid(column=1, row=2)
    six = Button(frm, text="6", height = 2, width = 5, font = 'Arial 24', command =lambda: add_button('6')).grid(column=2, row=2)
    seven = Button(frm, text="7", height = 2, width = 5, font = 'Arial 24', command =lambda: add_button('7')).grid(column=2, row=1)
    eight = Button(frm, text="8", height = 2, width = 5, font = 'Arial 24', command =lambda: add_button('8')).grid(column=1, row=1)
    nine = Button(frm, text="9", height = 2, width = 5, font = 'Arial 24',command =lambda: add_button('9')).grid(column=0, row=1)
    zero = Button(frm, text="0", height = 2, width = 5, font = 'Arial 24', command =lambda: add_button('0')).grid(column=0, row=4)
    plus = Button(frm, text="+", height = 2, width = 5, font = 'Arial 24', command =lambda: add_button('+')).grid(column=3, row=1)
    minus = Button(frm, text="-", height = 2, width = 5, font = 'Arial 24', command =lambda: add_button('-')).grid(column=3, row=2)
    mult = Button(frm, text="*", height = 2, width = 5, font = 'Arial 24', command =lambda: add_button('*')).grid(column=3, row=3)
    div = Button(frm, text="/", height = 2, width = 5, font = 'Arial 24', command =lambda: add_button('/')).grid(column=3, row=4)
    clr = Button(frm, text="clr", height = 2, width = 5, font = 'Arial 24', command =lambda: clear()).grid(column=1, row=4)
    equals = Button(frm, text="=", height = 2, width = 5, font = 'Arial 24', command =lambda: answer()).grid(column=2, row=4)

buttons()

root.mainloop()