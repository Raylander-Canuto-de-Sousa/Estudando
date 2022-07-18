#importando SQLite3
import sqlite3 as sql

#conectando ao banco ou criando e definindo o cursor
banco = sql.connect("inventario.db")
cursor = banco.cursor()

with banco:
    cursor.execute("CREATE TABLE IF NOT EXISTS estoque(id INTEGER PRIMARY KEY AUTOINCREMENT, nome_produto TEXT, quantidade_produto INT, categoria_produto TEXT, fornecedor_produtos TEXT, custo_produto REAL)")
    cursor.execute("CREATE TABLE IF NOT EXISTS cadastro(id INTEGER PRIMARY KEY AUTOINCREMENT, cpf VARCHAR(11), email TEXT, senha TEXT)")

def cadastrar(x):
    query = "INSERT INTO cadastro(cpf, email, senha) VALUES (?, ?, ?)"
    cursor.execute(query, x)
    banco.commit()

#CREATE
def inserir_produto(p):
    query = "INSERT INTO estoque(nome_produto, quantidade_produto, categoria_produto, fornecedor_produtos, custo_produto) VALUES (?, ?, ?, ?, ?)"
    cursor.execute(query, p)
    banco.commit()

#READY
def mostrar_produto():
    lista = []
    with banco:
        query = "SELECT * FROM estoque"
        cursor.execute(query)
        info = cursor.fetchall()
        print(info)
        for i in info:
            lista.append(i)
    return lista
    #banco.commit()

#UPDATE
def atualizar_produto(id):
    query = "UPDATE estoque SET nome_produto=?, quantidade_produto=?, categoria_produto=?, fornecedor_produtos=?, custo_produto=? WHERE id=?"
    cursor.execute(query, id)
    banco.commit()

#DELETE
def apagar_produto(id):
    query = "DELETE FROM estoque WHERE id=?"
    cursor.execute(query, id)
    banco.commit()

#inserindo produtos no inventario
def inserir_usuario(p):
    with banco:
        cursor = banco.cursor()
        query = "INSERT INTO cadastro(cpf, email, senha) VALUES (?, ?, ?)"
        cursor.execute(query, p)


#funções de verificação
def verificar_cpf(p):
    cursor.execute("SELECT cpf FROM cadastro")
    cpf = cursor.fetchall()
    for i in cpf:
        for i2 in i:
            if i2 == p:
                print("\ncpf puxado\n==> ", i2)
                return 1
    return 0

def verificar_email(p):
    cursor.execute("SELECT email FROM cadastro")
    email = cursor.fetchall()
    for i in email:
        for i2 in i:
            if i2 == p:
                print("\nemail puxado\n==> ", i2)
                return 1
    return 0

def verificar_senha(p, cpf, email):
    cursor.execute("SELECT senha FROM cadastro WHERE cpf = ? OR email = ?", (cpf, email))
    senha = cursor.fetchall()
    #print(senha)
    for i in senha:
        for i2 in i:
            if i2 == p:
                print("\nsenha puxada\n==> ", i2)
                return 1
    return 0

# verificar_cpf(78945612301)
# verificar_email("algumacoisa")
#verificar_senha("camadas","95174823605","blancoepleto@gmail.com4")