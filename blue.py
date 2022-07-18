from tkinter import Button, Entry, Frame, Label, Tk, Toplevel
from banco import cadastrar, verificar_cpf, verificar_email, verificar_senha

class janela:

    def novajanela(self, titulo, estado):
        self.janelanova = Toplevel(root)
        self.janelanova.title(titulo)
        self.janelanova.state(estado)
    
    def logar(self):
        user = self.ety_1.get()
        password = self.ety_2.get()
        veri = verificar_cpf(user) + verificar_email(user) + verificar_senha(password, user, user)

        if veri == 2:
            print("liberada tela de estoque")
        elif veri != 2:
            print("permição Negada")

    def __init__(self, tk):
        frame1 = Frame(tk).pack()
        ################################################ campos de login
        lbl_1 = Label(frame1, text="Digite seu CPF ou E-mail:").place(x=300, y=200)
        self.ety_1 = Entry(frame1); self.ety_1.place(x=450, y=200)

        lbl_2 = Label(frame1, text="Digite sua senha:").place(x=300, y=250)
        self.ety_2 = Entry(frame1, show="*"); self.ety_2.place(x=450, y=250)

        btn_1 = Button(frame1, text="logar", command=self.logar).place(x=300, y=300)
        btn_2 = Button(frame1, text="Cadastrar", command=self.cadastrar).place(x=350, y=300)
        ################################################ campos de login

    def inserir(self):
        #essa função pegara todas as entradas com ".get"
        cpf = str(self.ety_cadastrar_cpf.get())
        email = str(self.ety_cadastrar_email.get())
        senha = str(self.ety_cadastrar_senha.get())

        lista = [cpf, email, senha]
        cadastrar(lista)

    def cadastrar(self):
        self.novajanela("Cadastro de Funcionário", "zoomed")
        #self.janelanova.state("zoomed")

        lbl_cadastrar_cpf = Label(self.janelanova, text="Digite seu CPF:").place(x=300, y=200)
        self.ety_cadastrar_cpf = Entry(self.janelanova); self.ety_cadastrar_cpf.place(x=450, y=200)

        lbl_cadastrar_email = Label(self.janelanova, text="Digite seu E-mail:").place(x=300, y=250)
        self.ety_cadastrar_email = Entry(self.janelanova); self.ety_cadastrar_email.place(x=450, y=250)
        
        lbl_cadastrar_senha = Label(self.janelanova, text="Digite sua senha:").place(x=300, y=300)
        self.ety_cadastrar_senha = Entry(self.janelanova); self.ety_cadastrar_senha.place(x=450, y=300)
        
        btn_cadastrar = Button(self.janelanova, text="Cadastrar", command=self.inserir).place(x=300, y=350)


root = Tk()
root.title("Sistema de Gerenciamento de Estoque")
root.state("zoomed")
#root.geometry("500x500")
janela(root)
root.mainloop()