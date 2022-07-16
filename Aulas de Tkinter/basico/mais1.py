from tkinter import *

# anchor options: N/S/E/W/CENTER/NS...

janela = Tk()

janela.title("Curso de Tkinter")

janela.geometry("500x500")

texto1 = Label(janela, text="Texto 1\nlegenda 1", font="Arial 20",
        bd=5, relief="solid", width=20, height=2)

texto2 = Label(janela, text="Texto 2", font="Arial 10",
        bd=5, relief="solid", width=15, height=2, anchor=S)

texto1.pack()
texto2.pack()

janela.mainloop()
