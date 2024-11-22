from tkinter import*
from tkinter import ttk

from PIL.ImImagePlugin import number
from PyInstaller.loader.pyiboot01_bootstrap import entry

import calculator_logic as c

oper=""
first=0 #первая
second=0 #вторая
result=0

def calc():
    second = float(entry.get())
    if oper =="+":
        result = c.add(first, second)
    elif oper == "-":
        result = c.subtract(first, second)
    elif oper =="*":
        result = c.multiply(first, second)
    elif oper =="/":
        result = c.divide(first, second)


def enter_number(number):
    entry.insert(END, number())


def clear_number():
    entry.insert(0, END)


def set_operation(operation):
    global first
    global oper
    first=float(entry)# флоат превращает числа из поля ввода
    oper = operation
    entry.delete(0,END)



