from tkinter import *

def calcular():
    f = float(text_fah.get())
    c = (f - 32) * 5 / 9
    final_text.set(f"{c:.2f} graus celcius")


janela = Tk()

janela.title("Conversão de Graus")

label_fah = Label(janela, text="Graus Fahrenheit: ")
text_fah = Entry(janela)

final_text = StringVar()
label_cel = Label(janela, textvariable=final_text)

btn_calcular = Button(janela,text="Calcular", command=calcular)

label_fah.grid()
text_fah.grid()
label_cel.grid()
btn_calcular.grid()

janela.mainloop()
