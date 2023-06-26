from tkinter import *

def buttonPress (num):
    global equation_text
    equation_text = equation_text + str(num)
    equation_label.set(equation_text)
    
def equals():
    global equation_text
    try:
      total = str(eval(equation_text))
      equation_label.set(total)
    
      equation_text = total
    except SyntaxError:
        equation_label.set('Syntax Error')
        equation_text=''
    except ZeroDivisionError:
        equation_label.set('Arithmetic Error')
        equation_text=''
    
def clear ():
    global equation_text
    equation_label.set('')
    equation_text=''

window = Tk()
window.title('Calculator')
window.geometry("500x500")

equation_text = ""
equation_label = StringVar()

label = Label(window, textvariable=equation_label, font=('consolas', 20), bg='gray', width=24, height=2)
label.pack()

frame = Frame(window)
frame.pack()

button1 = Button(frame, text=1, height=4, width=9, font=35, command=lambda: buttonPress(1))
button1.grid(row= 0, column=0)

button2 = Button(frame, text=2, height=4, width=9, font=35, command=lambda: buttonPress(2))
button2.grid(row= 0, column=1)

button3 = Button(frame, text=3, height=4, width=9, font=35, command=lambda: buttonPress(3))
button3.grid(row= 0, column=2)

button4 = Button(frame, text=4, height=4, width=9, font=35, command=lambda: buttonPress(4))
button4.grid(row= 1, column=0)

button5 = Button(frame, text=5, height=4, width=9, font=35, command=lambda: buttonPress(5))
button5.grid(row= 1, column=1)

button6 = Button(frame, text=6, height=4, width=9, font=35, command=lambda: buttonPress(6))
button6.grid(row= 1, column=2)

button7 = Button(frame, text=7, height=4, width=9, font=35, command=lambda: buttonPress(7))
button7.grid(row= 2, column=0)

button8 = Button(frame, text=8, height=4, width=9, font=35, command=lambda: buttonPress(8))
button8.grid(row= 2, column=1)

button9 = Button(frame, text=9, height=4, width=9, font=35, command=lambda: buttonPress(9))
button9.grid(row= 2, column=2)

button0 = Button(frame, text=0, height=4, width=9, font=35, command=lambda: buttonPress(0))
button0.grid(row= 3, column=1)

Plus = Button(frame, text='+', height=4, width=9, font=35, command=lambda: buttonPress('+'))
Plus.grid(row= 3, column=0)

Minus = Button(frame, text='-', height=4, width=9, font=35, command=lambda: buttonPress('-'))
Minus.grid(row= 3, column=2)

Multiply = Button(frame, text='*', height=4, width=9, font=35, command=lambda: buttonPress('*'))
Multiply.grid(row= 0, column=3)

Divide = Button(frame, text='/', height=4, width=9, font=35, command=lambda: buttonPress('/'))
Divide.grid(row= 1, column=3)

Equal = Button(frame, text='=', height=4, width=9, font=35, command=equals)
Equal.grid(row= 2, column=3)

decimal = Button(frame, text='.', height=4, width=9, font=35, command=lambda: buttonPress('.'))
decimal.grid(row= 3, column=3)

Clear = Button(window, text='CE', height=4, width=15, font=35, command=clear)
Clear.pack()


window.mainloop()