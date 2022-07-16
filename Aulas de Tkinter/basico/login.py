from tkinter import *

janela = Tk()

janela.title("Login")


Label(janela, text="User: ").grid(column=0, row=0, sticky=W)
Label(janela, text="Password: ").grid(column=0, row=1)


user_aws = Entry(janela).grid(column=1, row=0)
password_aws = Entry(janela).grid(column=1, row=1)

btn_login = Button(janela, text="Login").grid(column=1, row=2,
        sticky=E)

janela.mainloop()
