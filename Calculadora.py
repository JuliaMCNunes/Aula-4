from tkinter import *


def num(valor):
    tela['text'] += valor


def resul():
    tela['text'] = eval(tela['text'])
    tela['text'] = str(tela['text'])


def limpaT():
    tela['text'] = ''


# def limpaU():


cal = Tk()
cal.geometry('250x300+800+260')
cal.grid_rowconfigure(0, weight=1)
cal.grid_rowconfigure(1, weight=1)
cal.grid_rowconfigure(2, weight=1)
cal.grid_rowconfigure(3, weight=1)
cal.grid_rowconfigure(4, weight=1)
cal.grid_rowconfigure(5, weight=1)
cal.grid_columnconfigure(0, weight=1)
cal.grid_columnconfigure(1, weight=1)
cal.grid_columnconfigure(2, weight=1)
cal.grid_columnconfigure(3, weight=1)


tela = Label(cal, text='')

b1 = Button(cal, text='0', font='Arial 13', bd=0.5, width=5, command=lambda: num('0'))
b2 = Button(cal, text='1', font='Arial 13', bd=0.5, width=5, command=lambda: num('1'))
b3 = Button(cal, text='2', font='Arial 13', bd=0.5, width=5, command=lambda: num('2'))
b4 = Button(cal, text='3', font='Arial 13', bd=0.5, width=5, command=lambda: num('3'))
b5 = Button(cal, text='4', font='Arial 13', bd=0.5, width=5, command=lambda: num('4'))
b6 = Button(cal, text='5', font='Arial 13', bd=0.5, width=5, command=lambda: num('5'))
b7 = Button(cal, text='6', font='Arial 13', bd=0.5, width=5, command=lambda: num('6'))
b8 = Button(cal, text='7', font='Arial 13', bd=0.5, width=5, command=lambda: num('7'))
b9 = Button(cal, text='8', font='Arial 13', bd=0.5, width=5, command=lambda: num('8'))
b10 = Button(cal, text='9', font='Arial 13', bd=0.5, width=5, command=lambda: num('9'))

b11 = Button(cal, text='=', font='Arial 15', bd=0.5, width=5, command=lambda: resul())
b12 = Button(cal, text='÷', font='Arial 15', bd=0.5, width=5, command=lambda: num('/'))
b13 = Button(cal, text='x', font='Arial 13', bd=0.5, width=5, command=lambda: num('*'))
b14 = Button(cal, text='-', font='Arial 15', bd=0.5, width=5, command=lambda: num('-'))
b15 = Button(cal, text='+', font='Arial 15', bd=0.5, width=5, command=lambda: num('+'))
b16 = Button(cal, text='.', font='Arial 15', bd=0.5, width=5, command=lambda: num('.'))
b19 = Button(cal, text='(', font='Arial 13', bd=0.5, width=5, command=lambda: num('('))
b20 = Button(cal, text=')', font='Arial 13', bd=0.5, width=5, command=lambda: num(')'))

b17 = Button(cal, text='C', font='Arial 13', bd=0.5, width=5, command=lambda: limpaT())
b18 = Button(cal, text='Del', font='Arial 13', bd=0.5, width=5)


tela.grid(row=0, rowspan=2, column=0, columnspan=4, sticky=NSEW)
b17.grid(row=3, column=0, sticky=NSEW)
b8.grid(row=4, column=0, sticky=NSEW)
b5.grid(row=5, column=0, sticky=NSEW)
b2.grid(row=6, column=0, sticky=NSEW)
b16.grid(row=7, column=0, sticky=NSEW)
b19.grid(row=3, column=1, sticky=NSEW)
b9.grid(row=4, column=1, sticky=NSEW)
b6.grid(row=5, column=1, sticky=NSEW)
b3.grid(row=6, column=1, sticky=NSEW)
b1.grid(row=7, column=1, sticky=NSEW)
b20.grid(row=3, column=2, sticky=NSEW)
b10.grid(row=4, column=2, sticky=NSEW)
b7.grid(row=5, column=2, sticky=NSEW)
b4.grid(row=6, column=2, sticky=NSEW)
b11.grid(row=7, column=2, sticky=NSEW)
b18.grid(row=3, column=3, sticky=NSEW)
b12.grid(row=4, column=3, sticky=NSEW)
b13.grid(row=5, column=3, sticky=NSEW)
b14.grid(row=6, column=3, sticky=NSEW)
b15.grid(row=7, column=3, sticky=NSEW)


cal.mainloop()
