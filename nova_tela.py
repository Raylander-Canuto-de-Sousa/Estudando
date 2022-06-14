# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 19:34:04 2022

@author: Aluno
"""

import tkinter as tk

def criarnovajanela():
    novajanela = tk.Toplevel(app)
    
app = tk.Tk()
app.state("zoomed")
botao  = tk.Button(app,text="Criar janela",command=criarnovajanela)


botao.pack()
app.mainloop()