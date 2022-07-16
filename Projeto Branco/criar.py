from random import randint
# from os import system
from tkinter import *
from tkinter import messagebox

# import erros
import filtrar
import gravar

def criar_conta(lista, nome, sobrenome, saldo):
    codigo = randint(10000, 99999)
    while True:
        if filtrar.contains(lista, codigo):
            codigo = randint(10000, 99999)
        else:
            break
    
    # Valores válidos: nome
    if nome.isnumeric():
        messagebox.showinfo(title="Erro", message="Sua informação de nome não deve ser um valor numérico")
        return 0
    elif sobrenome.isnumeric():
        messagebox.showinfo(title="Erro", message="Sua informação de sobrenome não deve ser um valor numérico")
        return 0
    elif nome == "":
        messagebox.showinfo(title="Erro", message="Sua informação de nome deve estar preenchida")
        return 0
    elif sobrenome == "":
        messagebox.showinfo(title="Erro", message="Sua informação de sobrenome deve estar preenchida")
        return 0

    nome_completo = nome + " " +sobrenome

    # Valores válidos: saldo
    if saldo == "":
        saldo = 0

    try:
        saldo = float(saldo)
        if saldo < 0:
            messagebox.showinfo(title="Erro", message="O saldo não pode ser negativo")      
            return 0
    except:
        messagebox.showinfo(title="Erro", message="O saldo deve ser um valor numérico")    
        return 0
 
    rsp = messagebox.askquestion(title="Confirmação", message="Confirmar criação da conta?")

    if rsp == "yes":
        # Gravar dados da conta
        obj = {}
        obj["id"] = codigo
        obj["nome"] = nome_completo
        obj["saldo"] = saldo

        lista.append(obj)

        gravar.gravar_dados(lista)
        
        messagebox.showinfo(title="Erro", message=f"Conta Criada! Seu código é: {codigo}")   

        return 0


def layout_criar_conta(lista, janela_menu):

    janela_criar_conta = Toplevel()
    janela_criar_conta.title("Criação de Conta")
    janela_criar_conta.geometry("600x460")
    janela_criar_conta["bg"] = "#dfe3ee"
    janela_criar_conta.transient(janela_menu)
    janela_criar_conta.focus_force()
    janela_criar_conta.grab_set()

    frame_criar_conta = Frame(janela_criar_conta, bg="#dfe3ee", highlightbackground="#1e3743", highlightcolor="#1e3743", 
                            highlightthickness=5, bd=0)   
    # Título
    title = Label(frame_criar_conta, text="Criar Conta", font="Verdana 17 bold", fg="#1e3743", bg="#dfe3ee")
    title.place(relwidth=0.45, relheight=0.17, relx=0.275)
 
    # Nome
    label_nome = Label(frame_criar_conta, text="Nome: ", bg="#dfe3ee", fg="#1e3743", font="Verdana 10 bold", anchor="w")
    label_nome.place(relx=0.1, rely=0.22, relheight=0.13, relwidth=0.17)

    entry_nome = Entry(frame_criar_conta, bd=0)
    entry_nome.focus_force()
    entry_nome.place(relx=0.28, rely=0.22, relheight=0.13, relwidth=0.62)
    
    # Sobrenome
    label_sobrenome = Label(frame_criar_conta, text="Sobrenome: ", bg="#dfe3ee", fg="#1e3743", font="Verdana 10 bold", anchor="w")
    label_sobrenome.place(relx=0.1, rely=0.39, relheight=0.13, relwidth=0.25)

    entry_sobrenome = Entry(frame_criar_conta, bd=0)
    entry_sobrenome.place(relx=0.39, rely=0.39, relheight=0.13, relwidth=0.51)

    # Saldo
    label_saldo = Label(frame_criar_conta, text="Saldo Inicial: ", fg="#1e3743", bg="#dfe3ee", font="Verdana 10 bold", anchor="w")
    label_saldo.place(relx=0.1, rely=0.56, relheight=0.13, relwidth=0.28)

    entry_saldo = Entry(frame_criar_conta, bd=0)
    entry_saldo.place(relx=0.39, rely=0.56, relheight=0.13, relwidth=0.51)

    # Botão
    btn_criar = Button(frame_criar_conta, text="Enviar", font="Verdana 10 bold",bg="#1e3743", fg="#dfe3ee", relief=FLAT,
                        highlightthickness=4, highlightbackground="#1e3743", activebackground="#dfe3ee", activeforeground="#1e3743",
                        command=lambda: criar_conta(lista, entry_nome.get(), entry_sobrenome.get(), entry_saldo.get()))
    btn_criar.place(relheight=0.16, relwidth=0.8, relx=0.1, rely=0.75)
    '''
    title = Label(frame_criar_conta, text="Criar Conta", font="Verdana 17 bold", fg="#1e3743", bg="#dfe3ee")
    title.place(relwidth=0.4, relheight=0.2, relx=0.3)

    label_nome = Label(frame_criar_conta, text="Nome: ", fg="#1e3743", bg="#dfe3ee", font="Verdana 10 bold", anchor="w")
    label_nome.place(relx=0.1, rely=0.25, relheight=0.15, relwidth=0.15)

    entry_nome = Entry(frame_criar_conta, bd=0)
    entry_nome.focus_force()
    entry_nome.place(relx=0.26, rely=0.25, relheight=0.15, relwidth=0.64)

    label_saldo = Label(frame_criar_conta, text="Saldo Inicial: ", fg="#1e3743", bg="#dfe3ee", font="Verdana 10 bold", anchor="w")
    label_saldo.place(relx=0.1, rely=0.45, relheight=0.15, relwidth=0.28)

    entry_saldo = Entry(frame_criar_conta, bd=0)
    entry_saldo.place(relx=0.39, rely=0.45, relheight=0.15, relwidth=0.51)

    btn_criar = Button(frame_criar_conta, text="Enviar", font="Verdana 10 bold",bg="#1e3743", fg="#dfe3ee", relief=FLAT,
                        highlightthickness=4, highlightbackground="#1e3743", activebackground="#dfe3ee", activeforeground="#1e3743",
                        command=lambda: criar_conta(lista, entry_nome.get(), entry_saldo.get()))
    btn_criar.place(relheight=0.2, relwidth=0.8, relx=0.1, rely=0.70)
    
    '''
    frame_criar_conta.place(rely=0.2, relx=0.15, relwidth=0.7, relheight=0.6)

    '''
    num = randint(10000, 99999)
    while True:
        if filtrar.contains(lista, num):
            num = randint(10000, 99999)
        else:
            break

    while True:
        nome_completo = input('Nome completo do usuário: ')
        if len(nome_completo) < 9:
            print('='*40)
            print("O nome digitado deve conter no mínimo 9 caracteres")
        elif not (" " in nome_completo[1:-1]):
            print('='*40)
            print("O nome deve conter ao menos um sobrenome")
        else:
            break

    while True:
        saldo = input('Saldo: ')
        try:
            saldo = float(saldo)
            if saldo < 0:
                print('='*40)
                print("Seu saldo não pode ser um valor negativo")
            else:
                break
        except:
            print('='*40)
            print("O saldo de ser um valor real")

    print('='*40)
    print('1 - Confirmar criação da da conta.')
    print('2 - Cancelar e voltar para o menu:')
    print('='*40)

    rsp = input('Escolha: ')
    rsp = erros.tratar_erro(rsp, "12")

    if rsp == "1":
        r = {'id': num, 'nome': nome_completo, 'saldo': saldo}
        lista.append(r)

        print('Conta criada com sucesso!')
        print(f'Seu número é {num}')
        print("Pressione qualquer tecla para retornar ao menu")
        print('='*40)
        voltar = input("Resposta: ")
    else:
        system("clear")
        return 0
    '''
