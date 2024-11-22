from tkinter import*
from tkinter import ttk
import calculator_logic as c

oper=""
first = 0 #первая
second = 0 #вторая
result = 0

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
    entry.delete(0, END)
    entry.insert(0,str(result))

def enter_number(number):
    entry.insert(END, number)


def clear_entry():
    entry.delete(0, END)


def set_operation(operation):
    global first
    global oper
    first=float(entry.get())# флоат превращает числа из поля ввода
    oper = operation
    entry.delete(0,END)


def validate_entry():
    e=entry.get()
    txt="".join(b for b in e if b in "0123456789.-")#склеиваем символы списка
    if e != txt: # если введенные значения не равны символам из переменной txt, то произойдет удаление
        entry.delete(0, END)
        entry.insert(0, txt)

window=Tk()
window.title("калькулятор")

entry = ttk.Entry()
entry.grid(row=0, column=0, columnspan=4, sticky="ew")
entry.bind("<KeyRelease>", lambda event: validate_entry())# запрещает вводить что-то другое в поле entry



ttk.Button(text="1", command=lambda: enter_number("1")).grid(row=1, column=0)
ttk.Button(text="2", command=lambda: enter_number("2")).grid(row=1, column=1)
ttk.Button(text="3", command=lambda: enter_number("3")).grid(row=1, column=2)
ttk.Button(text="4", command=lambda: enter_number("4")).grid(row=2, column=0)
ttk.Button(text="5", command=lambda: enter_number("5")).grid(row=2, column=1)
ttk.Button(text="6", command=lambda: enter_number("6")).grid(row=2, column=2)
ttk.Button(text="7", command=lambda: enter_number("7")).grid(row=3, column=0)
ttk.Button(text="8", command=lambda: enter_number("8")).grid(row=3, column=1)
ttk.Button(text="9", command=lambda: enter_number("9")).grid(row=3, column=2)
ttk.Button(text="0", command=lambda: enter_number("0")).grid(row=4, column=0)

ttk.Button(text="c", command=clear_entry).grid(row=4, column=1)
ttk.Button(text="=", command=calc).grid(row=4, column=2)

ttk.Button(text="+", command=lambda: set_operation("+")).grid(row=1, column=3)
ttk.Button(text="-", command=lambda: set_operation("-")).grid(row=2, column=3)
ttk.Button(text="*", command=lambda: set_operation("*")).grid(row=3, column=3)
ttk.Button(text="/", command=lambda: set_operation("/")).grid(row=4, column=3)




window.mainloop()