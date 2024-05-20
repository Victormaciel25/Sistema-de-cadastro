# Importando sqlite
import sqlite3 as lite

# Criando conexão
con = lite.connect('dados.db')

# CRUD

# Inserir dados
def inserir_form(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO inventario(nome,local, descricao, marca, data_da_compra,valor_da_compra, serie, imagem) VALUES(?,?,?,?,?,?,?,?)"
        cur.execute(query, dados)

atualizar_dados = ['Sofa', 'cozinha', 'sofa que comprei em 2001', 'Marca X', '27/08/2022', '500', 'xxxx', 'c:imagens', 1]

# Atualizar dados
with con:
    cur = con.cursor()
    query = "UPDATE inventario SET nome=?,local=?, descricao=?, marca=?, data_da_compra=?,valor_da_compra=?, serie=?, imagem=? WHERE id=?"
    cur.execute(query, atualizar_dados)
deletar_dados = str(2)

# Deletar dados
with con:
    cur = con.cursor()
    query = "DELETE FROM inventario WHERE id=?"
    cur.execute(query, deletar_dados)

ver_dados = []

# Ver dados
with con:
    cur = con.cursor()
    query = "SELECT * FROM inventario"
    cur.execute(query)

    rows = cur.fetchall()
    for row in rows:
        ver_dados.append(row)

ver_dados_individual = []

# Ver dados
with con:
    cur = con.cursor()
    query = "SELECT * FROM inventario WHERE id=?"
    cur.execute(query, id)

    rows = cur.fetchall()
    for row in rows:
        ver_dados_individual.append(row)