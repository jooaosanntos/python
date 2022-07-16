from tkinter import *

janela = Tk()

janela.geometry("500x500")
janela.title("Texto variável")

my_var = "Olé, mundo!"
label1 = Label(janela, text=my_var)

label2 = Label(janela, text="A")
label2["text"] = "ABC"

my_var2 = StringVar()
my_var2.set("Texto inicial")
label3 = Label(janela, textvariable=my_var2)
my_var2.set("Texto alterado depois!")


label1.pack()
label2.pack()
label3.pack()

janela.mainloop()
