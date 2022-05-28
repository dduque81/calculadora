from tkinter import *
from tkinter import PhotoImage
import tkinter as tk
import math

root = Tk()
root.title('Calculadora')

display = Entry(root)
display.grid(row=1, columnspan=6, sticky=W+E)

i = 0

def get_numbers(n):
    global i
    display.insert(i, n)
    i += 1

def get_operator(operator):
    global i
    op_length = len(operator)
    display.insert(i, operator)
    i += op_length

def clear_display():
    display.delete(0, END)

def undo():
    display_state = display.get()
    if len(display_state):
        display_new_state = display_state[:-1]  #Quito el ultimo elemento
        clear_display() #Borro todos los elementos
        display.insert(0, display_new_state) #Pongo la lista menos el ultimo elemento
    else:
        clear_display()

def calculate():
    display_state = display.get()
    try:
        math_expression = compile(display_state,'calculadora.py','eval')
        result = eval(math_expression)
        clear_display()
        display.insert(0, result)
    except:
        clear_display()
        display.insert(0,'Error')


#Buttons
Button(root, text='1', command = lambda:get_numbers(1), font=('Segoe UI', 14)).grid(row=2, column=0, sticky=W+E)
Button(root, text='2', command = lambda:get_numbers(2), font=('Segoe UI', 14)).grid(row=2, column=1, sticky=W+E)
Button(root, text='3', command = lambda:get_numbers(3), font=('Segoe UI', 14)).grid(row=2, column=2, sticky=W+E)

Button(root, text='4', command = lambda:get_numbers(4),font=('Segoe UI', 14)).grid(row=3, column=0, sticky=W+E)
Button(root, text='5', command = lambda:get_numbers(5),font=('Segoe UI', 14)).grid(row=3, column=1, sticky=W+E)
Button(root, text='6', command = lambda:get_numbers(6),font=('Segoe UI', 14)).grid(row=3, column=2, sticky=W+E)

Button(root, text='7', command = lambda:get_numbers(7),font=('Segoe UI', 14)).grid(row=4, column=0, sticky=W+E)
Button(root, text='8', command = lambda:get_numbers(8),font=('Segoe UI', 14)).grid(row=4, column=1, sticky=W+E)
Button(root, text='9', command = lambda:get_numbers(9),font=('Segoe UI', 14)).grid(row=4, column=2, sticky=W+E)

Button(root, text=' 0', command = lambda:get_numbers(0),font=('Segoe UI', 14)).grid(row=5, column=1, sticky=W+E)

#Botones aplicaciones
Button(root, text='AC', command=lambda: clear_display(),font=('Segoe UI', 14)).grid(row=5, column=0, sticky=W+E)
Button(root, text='%', command=lambda: get_operator('%'),font=('Segoe UI', 14)).grid(row=5, column=2, sticky=W+E)

#Botones operaciones
Button(root, text='+', command=lambda: get_operator('+'),font=('Segoe UI', 14)).grid(row=2, column=3, sticky=W+E)
Button(root, text='-', command=lambda: get_operator('-'),font=('Segoe UI', 14)).grid(row=2, column=4, sticky=W+E)
Button(root, text='/', command=lambda: get_operator('/'),font=('Segoe UI', 14)).grid(row=3, column=3, sticky=W+E)
Button(root, text='*', command=lambda: get_operator('*'),font=('Segoe UI', 14)).grid(row=3, column=4, sticky=W+E)
Button(root, text='(', command=lambda: get_operator('('),font=('Segoe UI', 14)).grid(row=4, column=3, sticky=W+E)
Button(root, text=')', command=lambda: get_operator(')'),font=('Segoe UI', 14)).grid(row=4, column=4, sticky=W+E)
Button(root, text='DEL', command = lambda: undo(),font=('Segoe UI', 14), bg='#e67f83').grid(row=5, column=3, sticky=W+E)
Button(root, text='exp', command=lambda: get_operator('**'),font=('Segoe UI', 14)).grid(row=5, column=4, sticky=W+E)
Button(root, text='^2', command=lambda: get_operator('**2'),font=('Segoe UI', 14)).grid(row=6, column=3, sticky=W+E)
Button(root, text='√', command=lambda: get_operator('math.sqrt('),font=('Segoe UI', 14)).grid(row=6, column=4, sticky=W+E)
Button(root, text='sin', command=lambda: get_operator('math.sin('),font=('Segoe UI', 14)).grid(row=6, column=0, sticky=W+E)
Button(root, text='cos', command=lambda: get_operator('math.cos('),font=('Segoe UI', 14)).grid(row=6, column=1, sticky=W+E)
Button(root, text='tan', command=lambda: get_operator('math.tan('),font=('Segoe UI', 14)).grid(row=6, column=2, sticky=W+E)
Button(root, text='=', command=lambda: calculate(),font=('Segoe UI', 14), bg='#ffbe67').grid(row=7, columnspan=6, sticky=W+E)
root.mainloop()