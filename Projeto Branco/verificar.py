from os import system
from tkinter import *
import erros

import filtrar

def verificar_conta(lista, janela_menu):
    
    janela_alterar_conta = Toplevel()
    janela_alterar_conta.transient(janela_menu)
    janela_alterar_conta.focus_force()
    janela_alterar_conta.grab_set()

    '''
    print('='*40)
    print('1 - Proseguir')
    print('2 - Voltar para o menu')
    print('='*40)
    rsp = input('Escolha: ')
    rsp = erros.tratar_erro(rsp, "12")
    print('='*40)
    if rsp == "1":
        while True:
            code = input('Número da conta: ')
            try:
                code = int(code)
                if filtrar.contains(lista, code):
                    break
                else:
                    print("O valor digitado não corresponde a uma conta válida")
            except:
                print("O valor digitado deve ser um número natural de 5 dígitos")
        
        index_code = filtrar.contains(lista, code, True)
        nome = lista[index_code]['nome']
        saldo = lista[index_code]['saldo']
        print(f'O Usuario {nome} tem o saldo de R$ {saldo:.2f}')
        print("Pressione qualquer tecla para retornar ao menu")
        print('='*40)
        voltar = input("Resposta: ")
    else:
        system("clear")
        return 0
    '''


