import datetime
import time

from classes import Biblioteca

ts = time.time()
timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')


def inserir_no_banco_livro(conexao, titulo, autor, ano):
    cursor = conexao.cursor()
    cursor.execute(
        "INSERT INTO livro (titulo, autor, ano_de_publicacao, dh_criacao) VALUES(%s, %s, %s, %s)",
        (titulo, autor, ano, timestamp)
    )
    conexao.commit()
    cursor.close()
    conexao.close()


def inserir_no_banco_biblioteca(conexao, nome, endereco):
    cursor = conexao.cursor()
    cursor.execute(
        "INSERT INTO biblioteca (nome, endereco, dh_criacao) VALUES(%s, %s, %s)",
        (nome, endereco, timestamp)
    )
    conexao.commit()
    cursor.close()
    conexao.close()

def consultar_bibliotecas(conexao):
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM biblioteca")
    bibliotecas = cursor.fetchall()

    for row in bibliotecas:
        print("Id = ", row[0], )
        print("Nome = ", row[1])
        print("Endereco  = ", row[2], "\n")



    list = []

    # appending instances to list
    list.append(Biblioteca('Maria', 'Rua Maria'))
    list.append(Biblioteca('Maria2', 'Rua Maria2'))
    list.append(Biblioteca('Maria3', 'Rua Maria3'))
    list.append(Biblioteca('Maria4', 'Rua Maria4'))
    list.append(Biblioteca('Maria5', 'Rua Maria5'))
    list.append(Biblioteca('Maria6', 'Rua Maria6'))

    bibliotecas = list;

    cursor.close()
    conexao.close()
    return bibliotecas

