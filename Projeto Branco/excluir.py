from os import system
from tkinter import *

import erros

import filtrar

def excluir_conta(lista, janela_menu):
    
    janela_excluir_conta = Toplevel()
    janela_excluir_conta.transient(janela_menu)
    janela_excluir_conta.focus_force()
    janela_excluir_conta.grab_set()

    '''
    print("=" * 40)
    print(f"{'Exclusão de conta':^40}")
    print("=" * 40)
    print("1 - Digitar código")
    print("2 - Voltar ao menu")

    rsp = input("Escolha: ")
    rsp = erros.tratar_erro(rsp, "12")

    if rsp == "1":
        while True:
            print("=" * 40)
            code = input("Código: ")
            print("=" * 40)
            try:
                code = int(code)
                if filtrar.contains(lista, code):
                    break
                else:
                    print("O valor digitado não correspende a uma conta válida")
            except:
                print("O valor digitado deve ser um número natural de 5 dígitos")
        index_code = filtrar.contains(lista, code, True)
        lista.pop(index_code)
        print("Conta excluída com sucesso!")
        print("Pressione qualquer tecla para retornar ao menu")
        print('='*40)
        voltar = input("Resposta: ")
    else:
        system("clear")
        return 0
    '''
