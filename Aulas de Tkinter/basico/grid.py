from tkinter import *

janela = Tk()

janela.title("Grid Layout")

label1 = Label(janela, text="Texto1", bg="purple")
label2 = Label(janela, text="Texto2", bg="yellow")
label3 = Label(janela, text="Texto3", bg="red")

label1.grid(row=0, column=0)
label2.grid(row=1, column=1)
label3.grid(row=2, column=2)

janela.mainloop()
