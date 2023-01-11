import re
from tkinter import *
from tkinter import messagebox
from tkinter import Tk
from tkinter.font import families

window = Tk()
window.title("Калькулятор")
window.iconbitmap("icon.ico")
window.geometry('928x571')
window['bg'] = '#f7f7f7'


def brackets(task):
    positions_of_brackets = []
    left_bracket_pos = -1
    for i in range(len(task)):
        if task[i] == '(' and i not in positions_of_brackets:
            left_bracket_pos = i
        elif task[i] == ')' and i not in positions_of_brackets and left_bracket_pos != -1:
            positions_of_brackets.append(left_bracket_pos)
            positions_of_brackets.append(i)
            # left_bracket_pos = -1
            break
    return positions_of_brackets


def processing(task):
    symbols = []

    for i in task:
        if i == '+' or i == '-' or i == '*' or i == '/':
            symbols.append(i)

    task = re.split(r'[-+/*]', task)

    if '' in task:
        # n = len(task)
        for i in range(len(task) - task.count('')):
            if task[i] == '':
                task[i] = str(0 - float(task[i + 1]))
                task.pop(i + 1)
                symbols.pop(i)

    for i in range(len(symbols)):
        j = 0
        temp = 0.0
        if '/' in symbols:
            j = symbols.index('/')
            symbols.remove('/')
            try:
                temp = float(task[j]) / float(task[j + 1])
            except ZeroDivisionError:
                pass

        elif '*' in symbols:
            j = symbols.index('*')
            symbols.remove('*')
            temp = float(task[j]) * float(task[j + 1])
        elif '-' in symbols:
            j = symbols.index('-')
            symbols.remove('-')
            temp = float(task[j]) - float(task[j + 1])
        elif '+' in symbols:
            j = symbols.index('+')
            symbols.remove('+')
            temp = float(task[j]) + float(task[j + 1])
        task.pop(j + 1)
        task[j] = temp

    return task[0]


def calculation():
    task = input_box.get().replace(',', '.')

    while True:
        pos = brackets(task)
        if not pos:
            task = float(processing(task))
            break
        else:
            temp = processing(task[(pos[0] + 1):pos[1]])
            task = task[0:pos[0]] + str(temp) + task[pos[1] + 1:len(task)]
        # pos = 1

    input_box.delete(0, len(input_box.get()))
    input_box.insert(0, str(task).replace('.', ','))


fart_color = '#000000'

input_box = Entry(font=("Segoe UI Semibold", 35), width=22, bg="#f7f7f7", selectbackground="#4c4a48", bd=0, justify=RIGHT)
input_box.place(x=0, y=75, width=594, height=65)
input_box.configure()
input_box.focus()

scrollbar = Scrollbar(window)
scrollbar.place(x=910, height=571)
memory = Listbox(window, font=("Segoe UI Semibold", 15), bg="#f7f7f7", selectbackground="#eaeaea",
                 selectforeground="#000000", bd=0, highlightthickness=0, height=17, justify=RIGHT, yscrollcommand=scrollbar.set)
memory.place(x=683, y=59)
scrollbar.config(command=memory.yview)



def add_symbol(number):
    input_box.insert(len(input_box.get()), number)


def delete_symbol():
    input_box.delete(len(input_box.get()) - 1)


def delete_all():
    input_box.delete(0, END)


def add_to_memory():
    memory.insert(0, input_box.get())


def get_from_memory():
    input_box.delete(0, END)
    try:
        input_box.insert(0, memory.get(memory.curselection()))
    except:
        input_box.insert(0, memory.get(0))


def clear_memory():
    memory.delete(0, END)


one = Button(text='1', font='Times 16', bg='#ffffff', highlightcolor='#000000', command=lambda: add_symbol(1))
two = Button(text='2', font='Times 16', bg='#ffffff', activebackground='#fbfbfb', command=lambda: add_symbol(2))
three = Button(text='3', font='Times 16', bg='#ffffff', activebackground='#fbfbfb', command=lambda: add_symbol(3))
four = Button(text='4', font='Times 16', bg='#ffffff', activebackground='#fbfbfb', command=lambda: add_symbol(4))
five = Button(text='5', font='Times 16', bg='#ffffff', activebackground='#fbfbfb', command=lambda: add_symbol(5))
six = Button(text='6', font='Times 16', bg='#ffffff', activebackground='#fbfbfb', command=lambda: add_symbol(6))
seven = Button(text='7', font='Times 16', bg='#ffffff', activebackground='#fbfbfb', command=lambda: add_symbol(7))
eight = Button(text='8', font='Times 16', bg='#ffffff', activebackground='#fbfbfb', command=lambda: add_symbol(8))
nine = Button(text='9', font='Times 16', bg='#ffffff', activebackground='#fbfbfb', command=lambda: add_symbol(9))
zero = Button(text='0', font='Times 16', bg='#ffffff', activebackground='#fbfbfb', command=lambda: add_symbol(0))
one.place(x=4, y=450, width=150, height=55)
two.place(x=156, y=450, width=150, height=55)
three.place(x=308, y=450, width=150, height=55)
four.place(x=4, y=393, width=150, height=55)
five.place(x=156, y=393, width=150, height=55)
six.place(x=308, y=393, width=150, height=55)
seven.place(x=4, y=336, width=150, height=55)
eight.place(x=156, y=336, width=150, height=55)
nine.place(x=308, y=336, width=150, height=55)
zero.place(x=156, y=507, width=150, height=55)

backspace = Button(text='←', font='Times 16', bg='#ffffff', activebackground='#fbfbfb', command=delete_symbol)
clear = Button(text='C', font='Times 16', bg='#ffffff', activebackground='#fbfbfb', command=delete_all)
division = Button(text='/', font='Times 16', bg='#ffffff', activebackground='#fbfbfb', command=lambda: add_symbol('/'))
multiplication = Button(text='*', font='Times 16', bg='#ffffff', activebackground='#fbfbfb', command=lambda: add_symbol('*'))
subtraction = Button(text='-', font='Times 16', bg='#ffffff', activebackground='#fbfbfb', command=lambda: add_symbol('-'))
addition = Button(text='+', font='Times 16', bg='#ffffff', activebackground='#fbfbfb', command=lambda: add_symbol('+'))
floating_point = Button(text=',', font='Times 16', bg='#ffffff', activebackground='#fbfbfb', command=lambda: add_symbol(','))
left_bracket = Button(text='(', font='Times 16', bg='#ffffff', activebackground='#fbfbfb', command=lambda: add_symbol('('))
right_bracket = Button(text=')', font='Times 16', bg='#ffffff', activebackground='#fbfbfb', command=lambda: add_symbol(')'))
memory_set = Button(text='MS', font='Times 16', bg='#ffffff', activebackground='#fbfbfb', command=add_to_memory)
memory_recall = Button(text='MR', font='Times 16', bg='#ffffff', activebackground='#fbfbfb', command=get_from_memory)
memory_clear = Button(text='MC', font='Times 16', bg='#ffffff', activebackground='#fbfbfb', command=clear_memory)
equal = Button(text='=', font='Times 16', bg='#363533', fg='#f9f9f9', activebackground='#5c5b59', activeforeground='#bebdbd', command=calculation)
fart = Button(text="fart", font='Times 16', fg=fart_color)

backspace.place(x=460, y=222, width=150, height=55)
clear.place(x=308, y=222, width=150, height=55)
division.place(x=460, y=279, width=150, height=55)
multiplication.place(x=460, y=336, width=150, height=55)
subtraction.place(x=460, y=393, width=150, height=55)
addition.place(x=460, y=450, width=150, height=55)
floating_point.place(x=308, y=507, width=150, height=55)
left_bracket.place(x=156, y=279, width=150, height=55)
right_bracket.place(x=308, y=279, width=150, height=55)
memory_set.place(x=4, y=222, width=150, height=55)
memory_recall.place(x=4, y=279, width=150, height=55)
memory_clear.place(x=156, y=222, width=150, height=55)
equal.place(x=460, y=507, width=150, height=55)
fart.place(x=4, y=507, width=150, height=55)

window.mainloop()

# TODO: запрет на ввод символов с клавиатуры кроме цифр и математических символов
# TODO: научить находить спаенные цифры с скобочками и вставлять туда *
# TODO: отлов ZeroDivisionError (+ прикольчик!)
# TODO: кнопка пердежа (прикольчик!)
# TODO: UNIT тесты............
