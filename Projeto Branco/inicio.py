from sys import exit
from os import system
from tkinter import *
import json

import erros

import criar
import alterar
import excluir
import verificar

with open('dados.json', 'r') as file:
    lista = json.load(file)

def menu():

    janela_menu = Tk()
    janela_menu.title("Banco Central")
    janela_menu["bg"] = "#dfe3ee"

    # Centralizar janela
    com_tela = janela_menu.winfo_screenwidth()
    lar_tela = janela_menu.winfo_screenheight()

    posx = (com_tela - 800) // 2
    posy = (lar_tela - 650) // 2

    str_pos = f"800x650+{posx}+{posy}"

    janela_menu.geometry(str_pos)    

    # Frame do menu
    frame_menu = Frame(janela_menu, padx=60, pady=10, bg="#dfe3ee",bd=5, highlightbackground="#1e3743", highlightthickness=5)

    frame_title = Label(frame_menu, text="Bem-Vindo!", font="Arial 25 bold", bg="#dfe3ee", fg="#1e3743")

    frame_title.pack()

    # Butões do menu
    btn_criar = Button(frame_menu, text="Criar conta", width=20, height=2, font="Verdana 12 bold", bg="#1e3743", fg="#dfe3ee",
                        command=lambda: criar.layout_criar_conta(lista, janela_menu),
                        relief=FLAT, highlightthickness=4, 
                        highlightbackground="#1e3743", activebackground="#dfe3ee", activeforeground="#1e3743")

    btn_alterar = Button(frame_menu, text="Alterar conta", width=20, height=2, font="Verdana 12 bold", bg="#1e3743", fg="#dfe3ee",
                        relief=FLAT, highlightthickness=4, highlightbackground="#1e3743", activebackground="#dfe3ee", 
                        activeforeground="#1e3743", command=lambda: alterar.layout_saldo(lista, janela_menu))

    btn_verificar = Button(frame_menu, text="Verificar conta", width=20, height=2, font="Verdana 12 bold", bg="#1e3743", fg="#dfe3ee",
                        relief=FLAT, highlightthickness=4,highlightbackground="#1e3743", activebackground="#dfe3ee",
                        activeforeground="#1e3743", command=lambda: verificar.verificar_conta(lista, janela_menu))

    btn_excluir = Button(frame_menu, text="Excluir conta", width=20, height=2, font="Verdana 12 bold", bg="#1e3743", fg="#dfe3ee",
                        relief=FLAT, highlightthickness=4, highlightbackground="#1e3743", activebackground="#dfe3ee",
                        activeforeground="#1e3743", command=lambda: excluir.excluir_conta(lista, janela_menu))
     
    btn_criar.pack(pady=20)
    btn_alterar.pack(pady=20)
    btn_verificar.pack(pady=20)
    btn_excluir.pack(pady=20)

    frame_menu.pack(pady=70)

    janela_menu.mainloop()
    
menu()
