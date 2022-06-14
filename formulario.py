from tkinter import * 
import sqlite3


###########################################################################
root = Tk()
root.state("zoomed")
root.geometry('500x230')
root.title("Formulário")
###########################################################################
fullname=StringVar()
email = StringVar()
var= IntVar()
c=StringVar()
var= IntVar()
###########################################################################
def database():
    name=fullname.get()
    conectar= sqlite3.connect('Form2.db')
    cursor=conectar.cursor()
    cursor.execute('CREATE TABLE IF NO EXISTS Student(fullname) VALUES(?)')
    cursor.execute('INSERT INTO Student (fullname) VALUES(?)',(nome,))
    conectar.commit()
    
    
###########################################################################

label_0 = Label(root, text="Formulário",width=20,font=("bold",20))
label_0.place(x=90, y=53)

label_1 = Label(root, text="Nome",width=20,font=("bold",10))
label_1.place(x=80,y=130)

entry_1 = Entry(root,textvar=fullname)
entry_1.place(x=240, y=130)

label_1 = Label(root, text="Email",width=20,font=("bold",10))
label_1.place(x=80,y=170)

entry_1 = Entry(root,textvar=email)
entry_1.place(x=240, y=170)
###########################################################################
list1=["China","Bulgaria","Japão","Korea"]

droplist=OpinionMenu(root,c,*list1)
droplist.config(width=15)
c.set("Selecione")
droplist.place(x=240,y=280)

label_4=Label(root,text="Programa", width=20,font=("bold",12))
label_4.place(x=70,y=330)
var2=IntVar()

checkbutton(root, text="Java",variable=var1).place(x=235,y=330)
checkbutton(root,text="python",variable=var1).place(x=290,y=330)

Radiobutton(root, text="Male",)

###########################################################################
    
Button(root, text='Submit',width=20,bg='brown',fg='white',command=database).place(x=180,y=480)

root.mainloop()