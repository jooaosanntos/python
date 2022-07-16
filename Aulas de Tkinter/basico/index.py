from tkinter import *

def func(msg):
    print(msg)

janela = Tk()

janela.title("Aula de Tkinter")
janela.attributes("-zoomed", True)

btn = Button(janela, text="Submit", command=lambda: func("Olá, mundo!"))
btn.pack()

janela.mainloop()
