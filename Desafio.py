from tkinter import *
import qrcode

###########################################################################

window = Tk()
window.state("zoomed")

dados_1 = StringVar()#Variavel que armazena dados do forms
dados_2 = StringVar()
###########################################################################

def qr():
    nome = dados_1.get()#chamando a variavel que guardou os dados do forms
    link = dados_2.get()
    image_qrcode = qrcode.make(link)
    image_qrcode.save(f"qrcode_{nome}.jpg")
    
    
###########################################################################

###########################################################################
lbl_name = Label(window,text="Nome do produto",width=20).place(x=300,y=80)
dados_name = Entry(window,textvar=dados_1).place(x=500,y=80)

lbl_link = Label(window,text="Link do produto",width=20).place(x=300,y=100)
dados_link = Entry(window,textvar=dados_2).place(x=500,y=100)#textvar envia os dados para uma variável

###########################################################################

btn = Button (window,text="submit",command=qr).place(x=400,y=300)

###########################################################################
window.mainloop()