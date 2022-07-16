from tkinter import *

class FrameForm(Frame):
    def __init__(self, element_father):
        super().__init__()
        self["height"] = 150
        self["width"] = 200
        self["bd"] = 2
        self["relief"] = SOLID
        self["padx"] = 20
        self["pady"] = 20

        label_nome = Label(self, text="Nome: ")
        text_nome = Entry(self)
        
        label_idade = Label(self, text="Idade: ")
        text_idade = Entry(self)

        btn_submit = Button(self, text="submit")

        label_nome.grid(column=0, row=0, pady=10)
        text_nome.grid(column=1, row=0)
 
        label_idade.grid(column=0, row=1, pady=10)
        text_idade.grid(column=1, row=1)

        btn_submit.grid(columnspan=2)

wd = Tk()

wd.geometry("700x700")
wd.title("Personal Widget")

frame_form1 = FrameForm(wd)
frame_form2 = FrameForm(wd)
frame_form3 = FrameForm(wd)

frame_form1.pack(pady=40)
frame_form2.pack(pady=40)
frame_form3.pack(pady=40)

wd.mainloop()
