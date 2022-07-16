from tkinter import *
from tkinter import messagebox

janela = Tk()

janela.attributes("-zoomed", True)

# Frame com Widgets
frame_form = Frame(janela, bd=2, relief="solid", pady=80, padx=80)

user_name = Label(frame_form, text="User: ")
user_password = Label(frame_form, text="Password: ")

text_name = Entry(frame_form)
text_password = Entry(frame_form)

a = messagebox.askquestion("Form", "Are you sure?")
print(a)
btn_submit = Button(frame_form, text="Login")

# Layout
user_name.grid(column=0, row=0, sticky="w")
user_password.grid(column=0, row=1, sticky="w")

text_name.grid(column=1, row=0)
text_name.focus()
text_password.grid(column=1, row=1)

btn_submit.grid(column=1, row=2, sticky="e")

frame_form.pack()

janela.mainloop()
