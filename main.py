import tkinter as tk
from tkinter import *

corTela = '#0d1b1f'
corFundo = '#5f686b'
corBotao = '#f5b400'
corTecla = '#ffffff'



janela = Tk()
janela.title('Conversor')
janela.geometry('300x150')
janela.config(bg=corFundo)

titulo = Frame(janela, width=300, height= 50, bg=corTecla)
titulo.grid(row=0, column=0)

opcao = Frame(janela, width=300, height=150, bg=corFundo)
opcao.grid(row=1, column=0)

tlabel = Label(titulo, text= 'Escolha uma conversão:', width=19, height=2, padx=7, relief=FLAT, anchor='e', justify=RIGHT, font=('Ivy 18 bold'))
tlabel.place(x=0, y=0)


allval = ''
valor = StringVar()

def abrirCF():
    janelaCF = Toplevel()
    janelaCF.title('Conversor Cº para Fº')
    janelaCF.geometry('235x313')
    janelaCF.config(bg=corFundo)

    tela = Frame(janelaCF, width=235, height=50, bg=corTela)
    tela.grid(row=0, column=0)

    fundo = Frame(janelaCF, width=235, height=268, bg=corFundo)
    fundo.grid(row=1, column=0)

    

    def inserir(event):
        global allval

        allval += str(event) 
        valor.set(allval)

    def calcular():
        global allval

        resultado = (float(allval)* (9/5)) + 32
        valor.set(str(resultado))

    def limpar():
        global allval

        allval = ''
        valor.set('')

    appLabel = Label(tela, textvariable=valor, width=16, height=2, padx=7, relief=FLAT, anchor='e', justify=RIGHT, font=('Ivy 18 '), bg=corTela, fg=corTecla)
    appLabel.place(x=0, y=0)


    #fileira um
    b1 = Button(fundo, command= limpar, text='C', width=18, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b1.place(x=0, y=0)
    b3 = Button(fundo, command = lambda: inserir('-'), text='-', width=5, height=2, bg=corBotao, fg=corTecla, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b3.place(x=177, y=0)

    #fileira dois
    b2 = Button(fundo, command = lambda: inserir('7'), text='7', width=7, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b2.place(x=0, y=53)
    b3 = Button(fundo, command = lambda: inserir('8'), text='8', width=7, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b3.place(x=78, y=53)
    b4 = Button(fundo, command = lambda: inserir('9'), text='9', width=7, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b4.place(x=155, y=53)

    #fileira tres
    b5 = Button(fundo, command = lambda: inserir('4'), text='4', width=7, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b5.place(x=0, y=106)
    b6 = Button(fundo, command = lambda: inserir('5'), text='5', width=7, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b6.place(x=78, y=106)
    b7 = Button(fundo, command = lambda: inserir('6'), text='6', width=7, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b7.place(x=155, y=106)

    #fileira quatro
    b8 = Button(fundo, command = lambda: inserir('1'), text='1', width=7, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b8.place(x=0, y=159)
    b9 = Button(fundo, command = lambda: inserir('2'), text='2', width=7, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b9.place(x=78, y=159)
    b10 = Button(fundo, command = lambda: inserir('3'), text='3', width=7, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b10.place(x=155, y=159)

    #fileira cinco
    b11 = Button(fundo, command = lambda: inserir('0'), text='0', width=11, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b11.place(x=0, y=212)
    b12 = Button(fundo, command = lambda: inserir('.'), text='.', width=5, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b12.place(x=118, y=212)
    b13 = Button(fundo, command= calcular, text='=', width=5, height=2, bg=corBotao, fg=corTecla, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b13.place(x=177, y=212)


def abrirCk():
    janelaCK = Toplevel()
    janelaCK.title('Conversor Cº para K')
    janelaCK.geometry('235x313')
    janelaCK.config(bg=corFundo)

    tela = Frame(janelaCK, width=235, height=50, bg=corTela)
    tela.grid(row=0, column=0)

    fundo = Frame(janelaCK, width=235, height=268, bg=corFundo)
    fundo.grid(row=1, column=0)

    

    def inserir(event):
        global allval

        allval += str(event) 
        valor.set(allval)

    def calcular():
        global allval

        resultado = float(allval) + 273.15
        valor.set(str(resultado))

    def limpar():
        global allval

        allval = ''
        valor.set('')

    appLabel = Label(tela, textvariable=valor, width=16, height=2, padx=7, relief=FLAT, anchor='e', justify=RIGHT, font=('Ivy 18 '), bg=corTela, fg=corTecla)
    appLabel.place(x=0, y=0)


    #fileira um
    b1 = Button(fundo, command= limpar, text='C', width=18, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b1.place(x=0, y=0)
    b3 = Button(fundo, command = lambda: inserir('-'), text='-', width=5, height=2, bg=corBotao, fg=corTecla, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b3.place(x=177, y=0)

    #fileira dois
    b2 = Button(fundo, command = lambda: inserir('7'), text='7', width=7, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b2.place(x=0, y=53)
    b3 = Button(fundo, command = lambda: inserir('8'), text='8', width=7, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b3.place(x=78, y=53)
    b4 = Button(fundo, command = lambda: inserir('9'), text='9', width=7, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b4.place(x=155, y=53)

    #fileira tres
    b5 = Button(fundo, command = lambda: inserir('4'), text='4', width=7, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b5.place(x=0, y=106)
    b6 = Button(fundo, command = lambda: inserir('5'), text='5', width=7, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b6.place(x=78, y=106)
    b7 = Button(fundo, command = lambda: inserir('6'), text='6', width=7, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b7.place(x=155, y=106)

    #fileira quatro
    b8 = Button(fundo, command = lambda: inserir('1'), text='1', width=7, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b8.place(x=0, y=159)
    b9 = Button(fundo, command = lambda: inserir('2'), text='2', width=7, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b9.place(x=78, y=159)
    b10 = Button(fundo, command = lambda: inserir('3'), text='3', width=7, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b10.place(x=155, y=159)

    #fileira cinco
    b11 = Button(fundo, command = lambda: inserir('0'), text='0', width=11, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b11.place(x=0, y=212)
    b12 = Button(fundo, command = lambda: inserir('.'), text='.', width=5, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b12.place(x=118, y=212)
    b13 = Button(fundo, command= calcular, text='=', width=5, height=2, bg=corBotao, fg=corTecla, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b13.place(x=177, y=212)


def abrirFK():
    janelaFK = Toplevel()
    janelaFK.title('Conversor Fº para K')
    janelaFK.geometry('235x313')
    janelaFK.config(bg=corFundo)

    tela = Frame(janelaFK, width=235, height=50, bg=corTela)
    tela.grid(row=0, column=0)

    fundo = Frame(janelaFK, width=235, height=268, bg=corFundo)
    fundo.grid(row=1, column=0)

    

    def inserir(event):
        global allval

        allval += str(event) 
        valor.set(allval)

    def calcular():
        global allval

        resultado = (float(allval) - 32) * 5/9 + 273.15
        valor.set(str(resultado))

    def limpar():
        global allval

        allval = ''
        valor.set('')

    appLabel = Label(tela, textvariable=valor, width=16, height=2, padx=7, relief=FLAT, anchor='e', justify=RIGHT, font=('Ivy 18 '), bg=corTela, fg=corTecla)
    appLabel.place(x=0, y=0)


    #fileira um
    b1 = Button(fundo, command= limpar, text='C', width=18, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b1.place(x=0, y=0)
    b3 = Button(fundo, command = lambda: inserir('-'), text='-', width=5, height=2, bg=corBotao, fg=corTecla, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b3.place(x=177, y=0)

    #fileira dois
    b2 = Button(fundo, command = lambda: inserir('7'), text='7', width=7, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b2.place(x=0, y=53)
    b3 = Button(fundo, command = lambda: inserir('8'), text='8', width=7, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b3.place(x=78, y=53)
    b4 = Button(fundo, command = lambda: inserir('9'), text='9', width=7, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b4.place(x=155, y=53)

    #fileira tres
    b5 = Button(fundo, command = lambda: inserir('4'), text='4', width=7, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b5.place(x=0, y=106)
    b6 = Button(fundo, command = lambda: inserir('5'), text='5', width=7, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b6.place(x=78, y=106)
    b7 = Button(fundo, command = lambda: inserir('6'), text='6', width=7, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b7.place(x=155, y=106)

    #fileira quatro
    b8 = Button(fundo, command = lambda: inserir('1'), text='1', width=7, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b8.place(x=0, y=159)
    b9 = Button(fundo, command = lambda: inserir('2'), text='2', width=7, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b9.place(x=78, y=159)
    b10 = Button(fundo, command = lambda: inserir('3'), text='3', width=7, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b10.place(x=155, y=159)

    #fileira cinco
    b11 = Button(fundo, command = lambda: inserir('0'), text='0', width=11, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b11.place(x=0, y=212)
    b12 = Button(fundo, command = lambda: inserir('.'), text='.', width=5, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b12.place(x=118, y=212)
    b13 = Button(fundo, command= calcular, text='=', width=5, height=2, bg=corBotao, fg=corTecla, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b13.place(x=177, y=212)
    

def abrirFC():
    janelaFC = Toplevel()
    janelaFC.title('Conversor Fº para Cº')
    janelaFC.geometry('235x313')
    janelaFC.config(bg=corFundo)

    tela = Frame(janelaFC, width=235, height=50, bg=corTela)
    tela.grid(row=0, column=0)

    fundo = Frame(janelaFC, width=235, height=268, bg=corFundo)
    fundo.grid(row=1, column=0)

    

    def inserir(event):
        global allval

        allval += str(event) 
        valor.set(allval)

    def calcular():
        global allval

        resultado = (float(allval) - 32) * 5/9
        valor.set(str(resultado))

    def limpar():
        global allval

        allval = ''
        valor.set('')

    appLabel = Label(tela, textvariable=valor, width=16, height=2, padx=7, relief=FLAT, anchor='e', justify=RIGHT, font=('Ivy 18 '), bg=corTela, fg=corTecla)
    appLabel.place(x=0, y=0)


    #fileira um
    b1 = Button(fundo, command= limpar, text='C', width=18, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b1.place(x=0, y=0)
    b3 = Button(fundo, command = lambda: inserir('-'), text='-', width=5, height=2, bg=corBotao, fg=corTecla, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b3.place(x=177, y=0)

    #fileira dois
    b2 = Button(fundo, command = lambda: inserir('7'), text='7', width=7, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b2.place(x=0, y=53)
    b3 = Button(fundo, command = lambda: inserir('8'), text='8', width=7, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b3.place(x=78, y=53)
    b4 = Button(fundo, command = lambda: inserir('9'), text='9', width=7, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b4.place(x=155, y=53)

    #fileira tres
    b5 = Button(fundo, command = lambda: inserir('4'), text='4', width=7, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b5.place(x=0, y=106)
    b6 = Button(fundo, command = lambda: inserir('5'), text='5', width=7, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b6.place(x=78, y=106)
    b7 = Button(fundo, command = lambda: inserir('6'), text='6', width=7, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b7.place(x=155, y=106)

    #fileira quatro
    b8 = Button(fundo, command = lambda: inserir('1'), text='1', width=7, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b8.place(x=0, y=159)
    b9 = Button(fundo, command = lambda: inserir('2'), text='2', width=7, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b9.place(x=78, y=159)
    b10 = Button(fundo, command = lambda: inserir('3'), text='3', width=7, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b10.place(x=155, y=159)

    #fileira cinco
    b11 = Button(fundo, command = lambda: inserir('0'), text='0', width=11, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b11.place(x=0, y=212)
    b12 = Button(fundo, command = lambda: inserir('.'), text='.', width=5, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b12.place(x=118, y=212)
    b13 = Button(fundo, command= calcular, text='=', width=5, height=2, bg=corBotao, fg=corTecla, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b13.place(x=177, y=212)
    

def abrirKC():
    janelaKC = Toplevel()
    janelaKC.title('Conversor K para Cº')
    janelaKC.geometry('235x313')
    janelaKC.config(bg=corFundo)

    tela = Frame(janelaKC, width=235, height=50, bg=corTela)
    tela.grid(row=0, column=0)

    fundo = Frame(janelaKC, width=235, height=268, bg=corFundo)
    fundo.grid(row=1, column=0)

    

    def inserir(event):
        global allval

        allval += str(event) 
        valor.set(allval)

    def calcular():
        global allval

        resultado = float(allval) - 273.15
        valor.set(str(resultado))

    def limpar():
        global allval

        allval = ''
        valor.set('')

    appLabel = Label(tela, textvariable=valor, width=16, height=2, padx=7, relief=FLAT, anchor='e', justify=RIGHT, font=('Ivy 18 '), bg=corTela, fg=corTecla)
    appLabel.place(x=0, y=0)


    #fileira um
    b1 = Button(fundo, command= limpar, text='C', width=18, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b1.place(x=0, y=0)
    b3 = Button(fundo, command = lambda: inserir('-'), text='-', width=5, height=2, bg=corBotao, fg=corTecla, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b3.place(x=177, y=0)

    #fileira dois
    b2 = Button(fundo, command = lambda: inserir('7'), text='7', width=7, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b2.place(x=0, y=53)
    b3 = Button(fundo, command = lambda: inserir('8'), text='8', width=7, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b3.place(x=78, y=53)
    b4 = Button(fundo, command = lambda: inserir('9'), text='9', width=7, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b4.place(x=155, y=53)

    #fileira tres
    b5 = Button(fundo, command = lambda: inserir('4'), text='4', width=7, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b5.place(x=0, y=106)
    b6 = Button(fundo, command = lambda: inserir('5'), text='5', width=7, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b6.place(x=78, y=106)
    b7 = Button(fundo, command = lambda: inserir('6'), text='6', width=7, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b7.place(x=155, y=106)

    #fileira quatro
    b8 = Button(fundo, command = lambda: inserir('1'), text='1', width=7, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b8.place(x=0, y=159)
    b9 = Button(fundo, command = lambda: inserir('2'), text='2', width=7, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b9.place(x=78, y=159)
    b10 = Button(fundo, command = lambda: inserir('3'), text='3', width=7, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b10.place(x=155, y=159)

    #fileira cinco
    b11 = Button(fundo, command = lambda: inserir('0'), text='0', width=11, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b11.place(x=0, y=212)
    b12 = Button(fundo, command = lambda: inserir('.'), text='.', width=5, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b12.place(x=118, y=212)
    b13 = Button(fundo, command= calcular, text='=', width=5, height=2, bg=corBotao, fg=corTecla, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b13.place(x=177, y=212)


def abrirKF():
    janelaKF = Toplevel()
    janelaKF.title('Conversor K para Fº')
    janelaKF.geometry('235x313')
    janelaKF.config(bg=corFundo)

    tela = Frame(janelaKF, width=235, height=50, bg=corTela)
    tela.grid(row=0, column=0)

    fundo = Frame(janelaKF, width=235, height=268, bg=corFundo)
    fundo.grid(row=1, column=0)

    

    def inserir(event):
        global allval

        allval += str(event) 
        valor.set(allval)

    def calcular():
        global allval

        resultado = (float(allval) - 273.15) * 9/5 + 32
        valor.set(str(resultado))

    def limpar():
        global allval

        allval = ''
        valor.set('')

    appLabel = Label(tela, textvariable=valor, width=16, height=2, padx=7, relief=FLAT, anchor='e', justify=RIGHT, font=('Ivy 18 '), bg=corTela, fg=corTecla)
    appLabel.place(x=0, y=0)


    #fileira um
    b1 = Button(fundo, command= limpar, text='C', width=18, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b1.place(x=0, y=0)
    b3 = Button(fundo, command = lambda: inserir('-'), text='-', width=5, height=2, bg=corBotao, fg=corTecla, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b3.place(x=177, y=0)

    #fileira dois
    b2 = Button(fundo, command = lambda: inserir('7'), text='7', width=7, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b2.place(x=0, y=53)
    b3 = Button(fundo, command = lambda: inserir('8'), text='8', width=7, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b3.place(x=78, y=53)
    b4 = Button(fundo, command = lambda: inserir('9'), text='9', width=7, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b4.place(x=155, y=53)

    #fileira tres
    b5 = Button(fundo, command = lambda: inserir('4'), text='4', width=7, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b5.place(x=0, y=106)
    b6 = Button(fundo, command = lambda: inserir('5'), text='5', width=7, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b6.place(x=78, y=106)
    b7 = Button(fundo, command = lambda: inserir('6'), text='6', width=7, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b7.place(x=155, y=106)

    #fileira quatro
    b8 = Button(fundo, command = lambda: inserir('1'), text='1', width=7, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b8.place(x=0, y=159)
    b9 = Button(fundo, command = lambda: inserir('2'), text='2', width=7, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b9.place(x=78, y=159)
    b10 = Button(fundo, command = lambda: inserir('3'), text='3', width=7, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b10.place(x=155, y=159)

    #fileira cinco
    b11 = Button(fundo, command = lambda: inserir('0'), text='0', width=11, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b11.place(x=0, y=212)
    b12 = Button(fundo, command = lambda: inserir('.'), text='.', width=5, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b12.place(x=118, y=212)
    b13 = Button(fundo, command= calcular, text='=', width=5, height=2, bg=corBotao, fg=corTecla, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    b13.place(x=177, y=212)



bCF = Button(opcao, command = abrirCF, text='Cº -> Fº', width=8, height=2)
bCF.grid(row=0, column=0)
bCF.place(x=4, y=5)
bCK = Button(opcao, command = abrirCk, text='Cº -> K', width=8, height=2)
bCK.grid(row=0, column=0)
bCK.place(x=120,y=5)
bFK = Button(opcao, command = abrirFK, text='Fº -> K', width=8, height=2)
bFK.grid(row=0, column=0)
bFK.place(x=230,y=5)
bFC = Button(opcao, command = abrirFC, text='Fº -> Cº', width=8, height=2)
bFC.grid(row=0, column=0)
bFC.place(x=4,y=50)
bKC = Button(opcao, command = abrirKC, text='k -> Cº', width=8, height=2)
bKC.grid(row=0, column=0)
bKC.place(x=120,y=50)
bKF = Button(opcao, command = abrirKF, text='K -> Fº', width=8, height=2)
bKF.grid(row=0, column=0)
bKF.place(x=230,y=50)

janela.mainloop()