from tkinter import *

janela = Tk()

janela.title("Column Span")


Label(janela, bg="red", width=20).grid(column=0)
Label(janela, bg="blue", width=20).grid(column=1)
Label(janela, bg="green", width=40).grid(columnspan=2, sticky="we")

janela.mainloop()
