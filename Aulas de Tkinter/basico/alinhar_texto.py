from tkinter import *

janela = Tk()

janela.geometry("1000x600")
janela.title("Alinhar texto")

label1 = Label(janela, text="O texto 1 se encontra\nnesse campo", 
        font="Verdana 10", bd=5, relief="solid", padx=20, pady=50,
        anchor=E, width=50, height=2)

label2 = Label(janela, text="O texto 1 se encontra\nnesse campo", 
        font="Verdana 20", bd=5, relief="solid", padx=20, pady=50,
        anchor=E, width=50, height=2, justify=LEFT)

label1.pack()
label2.pack()

print(label1["height"], label2["justify"])

janela.mainloop()
