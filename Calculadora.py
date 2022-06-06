from tkinter import *


def num(valor):
    tela['text'] += valor


def resul():
    entrada = tela['text']
    entrada1 = entrada.replace('/', '~').replace('*', '~').replace('-', '~').replace('+', '~')
    entrada2 = entrada1.split('~')
    controle = 0
    for i in range(len(entrada2)):
        if not entrada2[i].replace('.', '1', 1).isnumeric():
            controle = 1
            break
    if controle == 0:
        tela['text'] = eval(tela['text'])
        tela['text'] = str(tela['text'])
    else:
        tela['text'] = 'Formato Inválido!'


def limpaT():
    tela['text'] = ''


def limpaU():
    tela['text'] = tela['text'][:-1]


cal = Tk()
cal.geometry('250x300+800+260')
cal.grid_rowconfigure(0, weight=1)
cal.grid_rowconfigure(1, weight=1)
cal.grid_rowconfigure(2, weight=1)
cal.grid_rowconfigure(3, weight=1)
cal.grid_rowconfigure(4, weight=1)
cal.grid_rowconfigure(5, weight=1)
cal.grid_rowconfigure(6, weight=1)
cal.grid_columnconfigure(0, weight=1)
cal.grid_columnconfigure(1, weight=1)
cal.grid_columnconfigure(2, weight=1)
cal.grid_columnconfigure(3, weight=1)
cal.bind('0', lambda event: num('0'))
cal.bind('1', lambda event: num('1'))
cal.bind('2', lambda event: num('2'))
cal.bind('3', lambda event: num('3'))
cal.bind('4', lambda event: num('4'))
cal.bind('5', lambda event: num('5'))
cal.bind('6', lambda event: num('6'))
cal.bind('7', lambda event: num('7'))
cal.bind('8', lambda event: num('8'))
cal.bind('9', lambda event: num('9'))
cal.bind('/', lambda event: num('/'))
cal.bind('*', lambda event: num('*'))
cal.bind('-', lambda event: num('-'))
cal.bind('+', lambda event: num('+'))
cal.bind('.', lambda event: num('.'))
cal.bind('<Return>', lambda event: resul())
cal.bind('(', lambda event: num('('))
cal.bind(')', lambda event: num(')'))
cal.bind('<Escape>', lambda event: limpaT())
cal.bind('<BackSpace>', lambda event: limpaU())


tela = Label(cal, text='', font='Arial 15')

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
b18 = Button(cal, text='Del', font='Arial 13', bd=0.5, width=5, command=lambda: limpaU())


tela.grid(row=0, rowspan=1, column=0, columnspan=4, sticky=NSEW)
b17.grid(row=2, column=0, sticky=NSEW)
b8.grid(row=3, column=0, sticky=NSEW)
b5.grid(row=4, column=0, sticky=NSEW)
b2.grid(row=5, column=0, sticky=NSEW)
b16.grid(row=6, column=0, sticky=NSEW)
b19.grid(row=2, column=1, sticky=NSEW)
b9.grid(row=3, column=1, sticky=NSEW)
b6.grid(row=4, column=1, sticky=NSEW)
b3.grid(row=5, column=1, sticky=NSEW)
b1.grid(row=6, column=1, sticky=NSEW)
b20.grid(row=2, column=2, sticky=NSEW)
b10.grid(row=3, column=2, sticky=NSEW)
b7.grid(row=4, column=2, sticky=NSEW)
b4.grid(row=5, column=2, sticky=NSEW)
b11.grid(row=6, column=2, sticky=NSEW)
b18.grid(row=2, column=3, sticky=NSEW)
b12.grid(row=3, column=3, sticky=NSEW)
b13.grid(row=4, column=3, sticky=NSEW)
b14.grid(row=5, column=3, sticky=NSEW)
b15.grid(row=6, column=3, sticky=NSEW)


cal.mainloop()
