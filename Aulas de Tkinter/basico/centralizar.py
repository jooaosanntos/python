from tkinter import *

janela = Tk()

janela.title("Centralização")

largura = 500
altura = 300

largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()

posx = int((largura_tela - largura) / 2)
posy = int((altura_tela - altura) / 2)

rsp = f"{largura}x{altura}+{posx}+{posy}"

janela.geometry(rsp)

texto1 = Label(janela, text="Texto 1", bg="#5b0055", fg="white", font="sans-serif 25 italic bold", bd=5, relief="solid")
texto2 = Label(janela, text="Texto 2", bg="#5b0055", fg="white", font="Arial 10 bold", width=40, height=10)
btn = Button(janela, text="Submit")

texto1.pack()
texto2.pack()
btn.pack()

janela.mainloop()
