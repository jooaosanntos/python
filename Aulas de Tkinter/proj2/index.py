from tkinter import *
from tkinter import ttk

root = Tk()

class App():

    def __init__(self):

        self.root = root
        self.tela()
        self.frames_da_tela()
        self.widgets_frame1()
        root.mainloop()

    def tela(self):

        self.root.title("Cadastro de Clientes")
        self.root["bg"] = "#1e3743"
        self.root.geometry("700x500")
        self.root.resizable(True, True)
        # self.root.maxsize(width=900, height=700)
        self.root.minsize(width=700, height=500)

    def frames_da_tela(self):

        self.frame_1 = Frame(self.root, bd=4, bg="#dfe3ee", 
                            highlightbackground="#759fe6", highlightthickness=3)

        self.frame_1.place(relx=0.02,rely=0.02, relwidth=0.96, relheight=0.56)
        
        self.frame_2 = Frame(self.root, bd=4, bg="#dfe3ee", 
                            highlightbackground="#759fe6", highlightthickness=3)
        self.frame_2.place(relx=0.02,rely=0.60, relwidth=0.96, relheight=0.36)

    def widgets_frame1(self):

        # Botão Limpar
        self.bt_limpar = Button(self.frame_1, text="Limpar", bg="#dfe3ee", fg="#1e3743", font="Verdana 8 bold",
                                bd=0, relief=FLAT,highlightthickness=4, highlightbackground="#1e3743", borderwidth=4,
                                activeforeground="#dfe3ee", activebackground="#1e3743")

        self.bt_limpar.place(relx=0.25, rely=0.15, relwidth=0.1, relheight=0.1)
        # Botão Buscar
        self.bt_buscar = Button(self.frame_1, text="Buscar", bg="#1e3743", fg="#dfe3ee", font="Verdana 8 bold",
                                bd=0, relief=FLAT,highlightthickness=4, highlightbackground="#1e3743", borderwidth=4,
                                activeforeground="#1e3743", activebackground="#dfe3ee")

        self.bt_buscar.place(relx=0.35, rely=0.15, relwidth=0.1, relheight=0.1)
        
        # Botão Novo
        self.bt_novo = Button(self.frame_1, text="Novo", bg="#1e3743", fg="#dfe3ee", font="Verdana 8 bold",
                                bd=0, relief=FLAT,highlightthickness=4, highlightbackground="#1e3743", borderwidth=4,
                                activebackground="#dfe3ee", activeforeground="#1e3743")
        self.bt_novo.place(relx=0.62, rely=0.15, relwidth=0.1, relheight=0.1)
        # Botão Alterar
        self.bt_alterar = Button(self.frame_1, text="Alterar", bg="#dfe3ee", fg="#1e3743", font="Verdana 8 bold",
                                bd=0, relief=FLAT,highlightthickness=4, highlightbackground="#1e3743", borderwidth=4,
                                activebackground="#1e3743", activeforeground="#dfe3ee")
        self.bt_alterar.place(relx=0.72, rely=0.15, relwidth=0.1, relheight=0.1)
        # Botão Apagar
        self.bt_apagar = Button(self.frame_1, text="Apagar", bg="#1e3743", fg="#dfe3ee", font="Verdana 8 bold",
                                bd=0, relief=FLAT,highlightthickness=4, highlightbackground="#1e3743", borderwidth=4,
                                activebackground="#dfe3ee", activeforeground="#1e3743")
        self.bt_apagar.place(relx=0.82, rely=0.15, relwidth=0.1, relheight=0.1)
        
        # Label e entrada de código
        self.lb_codigo = Label(self.frame_1, text="Código", bg="#dfe3ee", anchor=W, font="Verdana 10 bold", fg="#1e3743")
        self.lb_codigo.place(relx=0.08, rely=0.02, relwidth=0.1, relheight=0.1)

        self.entry_codigo = Entry(self.frame_1)
        self.entry_codigo.place(relx=0.08, rely=0.15, relwidth=0.1, relheight=0.1)

        # Label e entrada de nome
        self.lb_nome = Label(self.frame_1, text="Nome", bg="#dfe3ee", anchor=W, font="Verdana 10 bold", fg="#1e3743")
        self.lb_nome.place(relx=0.08, rely=0.28, relwidth=0.1, relheight=0.1)

        self.entry_nome = Entry(self.frame_1)
        self.entry_nome.place(relx=0.08, rely=0.41, relwidth=0.84, relheight=0.1)
        
        # Label e entrada de telefone
        self.lb_telefone = Label(self.frame_1, text="Telefone", bg="#dfe3ee", anchor=W, font="Verdana 10 bold", fg="#1e3743")
        self.lb_telefone.place(relx=0.08, rely=0.54, relwidth=0.1, relheight=0.1)

        self.entry_telefone = Entry(self.frame_1)
        self.entry_telefone.place(relx=0.08, rely=0.67, relwidth=0.38, relheight=0.1)
         
        # Label e entrada de cidade
        self.lb_cidade = Label(self.frame_1, text="Cidade", bg="#dfe3ee", anchor=W, font="Verdana 10 bold", fg="#1e3743")
        self.lb_cidade.place(relx=0.54, rely=0.54, relwidth=0.1, relheight=0.1)

        self.entry_cidade = Entry(self.frame_1)
        self.entry_cidade.place(relx=0.54, rely=0.67, relwidth=0.38, relheight=0.1)

    def lista_frame2(self):
        self.listaCli = ttk.Treeview(self.frame_2, height=3, column=("col1", "col2", "col3", "col4"))


App()
