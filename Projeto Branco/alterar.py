# from os import system
from tkinter import *
from tkinter import messagebox

# import erros
import gravar
import filtrar

def alterar_conta(lista, codigo, valor, escolha):

    # Código válido
    try:
        codigo = int(codigo) 
        if not (filtrar.contains(lista, codigo)):
            messagebox.showinfo(title="Erro", message="O código digitado não corresponde a uma conta válida")
            return 0
    except:
        if codigo == "":
            messagebox.showinfo(title="Erro", message="Digite o valor do código da sua conta")
            return 0
        else:
            messagebox.showinfo(title="Erro", message="O valor digitado deve ser um número natural")
            return 0
    
    # Valor válido
    try:
        valor = float(valor)
        if valor < 1:
            messagebox.showinfo(title="Erro", message="Você só pode depositar ou sacar, no mínimo, 1 real")
            return 0
    except:
        if valor == "":
            messagebox.showinfo(title="Erro", message="Digite o valor a ser sacado ou depositado")
            return 0
        else:
            messagebox.showinfo(title="Erro", message="O valor a ser depositado ou sacado deve ser um valor numérico")
            return 0

    # Escolha
    index_codigo = filtrar.contains(lista, codigo, True)
    cliente = lista[index_codigo]["nome"]

    if escolha == 1:
        rsp = messagebox.askquestion(title="Confirmação", message=f"Confirmar saque de R$ {valor:.2f}?")
        if rsp == "yes":
            lista[index_codigo]["saldo"] -= valor
            saldo_atual = lista[index_codigo]["saldo"]
            gravar.gravar_dados(lista)
            messagebox.showinfo(title="Sucesso", message=f"{cliente}, seu saque foi realizado com sucesso! Seu saldo atual é de R$ {saldo_atual:.2f}")
            return 0
    elif escolha == 2:
        rsp = messagebox.askquestion(title="Confirmação", message=f"Confirmar depósito de R$ {valor:.2f}?")
        if rsp == "yes":
            lista[index_codigo]["saldo"] += valor
            saldo_atual = lista[index_codigo]["saldo"]
            # Gravar dados
            gravar.gravar_dados(lista)
            messagebox.showinfo(message=f"{cliente}, seu depósito foi realizado com sucesso! Seu saldo atual é de R$ {saldo_atual:.2f}",
                                title="Sucesso")
            return 0


def layout_saldo(lista, janela_menu):
     
    janela_alterar_conta = Toplevel()
    janela_alterar_conta.title("Criação de Conta")
    janela_alterar_conta.geometry("600x430")
    janela_alterar_conta["bg"] = "#dfe3ee"
    janela_alterar_conta.transient(janela_menu)
    janela_alterar_conta.focus_force()
    janela_alterar_conta.grab_set()

    frame_alterar_conta = Frame(janela_alterar_conta, bg="#dfe3ee", highlightbackground="#1e3743", highlightcolor="#1e3743", 
                                highlightthickness=5, bd=0) 
    # Título
    title = Label(frame_alterar_conta, text="Alterar Conta", font="Verdana 17 bold", fg="#1e3743", bg="#dfe3ee")
    title.place(relwidth=0.45, relheight=0.17, relx=0.275)
 
    # Código
    label_codigo = Label(frame_alterar_conta, text="Código: ", bg="#dfe3ee", fg="#1e3743", font="Verdana 10 bold", anchor="w")
    label_codigo.place(relx=0.1, rely=0.22, relheight=0.14, relwidth=0.17)

    entry_codigo = Entry(frame_alterar_conta, bd=0)
    entry_codigo.focus_force()
    entry_codigo.place(relx=0.28, rely=0.22, relheight=0.14, relwidth=0.62)
    
    # Valor
    label_valor = Label(frame_alterar_conta, text="Valor: ", bg="#dfe3ee", fg="#1e3743", font="Verdana 10 bold", anchor="w")
    label_valor.place(relx=0.1, rely=0.39, relheight=0.14, relwidth=0.15)

    entry_valor = Entry(frame_alterar_conta, bd=0)
    entry_valor.place(relx=0.28, rely=0.39, relheight=0.14, relwidth=0.62)

    # Radio
    escolha = IntVar()
    radio_sacar = Radiobutton(frame_alterar_conta, text="Sacar", variable=escolha, value=1, fg="#1e3743", bg="#dfe3ee", 
                                font="Verdana 10 bold", anchor="w")
    radio_sacar.select()
    radio_sacar.place(relx=0.1, rely=0.56, relheight=0.14, relwidth=0.28)

    radio_depositar = Radiobutton(frame_alterar_conta, text="Depositar", variable=escolha, value=2, fg="#1e3743", bg="#dfe3ee", 
                            font="Verdana 10 bold")
    radio_depositar.place(relx=0.4, rely=0.56, relheight=0.14, relwidth=0.28)

    # Botão
    btn_alterar = Button(frame_alterar_conta, text="Alterar", font="Verdana 10 bold",bg="#1e3743", fg="#dfe3ee", relief=FLAT,
                        highlightthickness=4, highlightbackground="#1e3743", activebackground="#dfe3ee", activeforeground="#1e3743",
                        command=lambda: alterar_conta(lista, entry_codigo.get(), entry_valor.get(), escolha.get()))
    btn_alterar.place(relheight=0.16, relwidth=0.8, relx=0.1, rely=0.73)

    frame_alterar_conta.place(rely=0.2, relx=0.15, relwidth=0.75, relheight=0.6)

    '''
    print("=" * 40)
    print(f"{'Alteração de Saldo':^40}")
    print("=" * 40)
    print("1 - Digitar código")
    print("2 - Voltar ao Menu")
    
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
                    print("O código digitado não correstponde a uma cnta válida")
            except:
                print("O valor digitado deve ser um número natural")
        print("=" * 40)
        print(f"{'Opções':^40}")
        print("1 - Depositar")
        print("2 - Sacar")
        print("=" * 40)

        opcao = input("Escolha: ")
        opcao = erros.tratar_erro(opcao, "12")

        if opcao == "1":
            while True:
                print("=" * 40)
                valor = input("Digite o valor a ser depositado: ")
                print("=" * 40)
                try:
                    valor = float(valor)
                    if valor < 1:
                        print("Você só pode depositar, no mínimo, 1 real")
                    else:
                        break
                except:
                    print("O valor a ser depositado deve ser um valor real")
            index_code = filtrar.contains(lista, code, True)
            lista[index_code]["saldo"] += valor
            print("Valor depositado com sucesso!")
            print("Pressione qualquer tecla para retornar ao menu")
            print('='*40)
            voltar = input("Resposta: ")
        else:
            while True:
                print("=" * 40)
                valor = input("Digite o valor a ser sacado: ")
                print("=" * 40)
                try:
                    valor = float(valor)
                    if valor < 1:
                        print("Você só pode sacar, no mínimo, 1 real")
                    else:
                        break
                except:
                    print("O valor a ser sacado deve ser um valor real") 
            
            index_code = filtrar.contains(lista, code, True)
            lista[index_code]["saldo"] -= valor
            print("Valor sacado com sucesso!")
            print("Pressione qualquer tecla para retornar ao menu")
            print('='*40)
            voltar = input("Resposta: ")
    else:
        system("clear")
        return 0
    '''
