import datetime
import time

from classes import Biblioteca, Livro

ts = time.time()
timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')


def inserir_no_banco_livro(conexao, titulo, autor, ano):
    cursor = conexao.cursor()
    cursor.execute(
        "INSERT INTO livro (titulo, autor, ano_de_publicacao, dh_criacao, biblioteca_id) VALUES(%s, %s, %s, %s, %s)",
        (titulo, autor, ano, timestamp, '1')
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
    linhas = cursor.fetchall()

    list = []
    for linha in linhas:
    # appending instances to list
        list.append(Biblioteca(linha[1], linha[2]))

    linhas = list

    cursor.close()
    return linhas



def consultar_livros(conexao):
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM livro")
    linhas = cursor.fetchall()

    list = []
    for linha in linhas:
    # appending instances to list
        livro = Livro(linha[0], linha[1], linha[2], linha[3], linha[7])

        list.append(livro)


    cursor.close()
    conexao.close()
    return list

def deletar_livro(conexao, id):
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM livro WHERE id = %s", (id))
    cursor.rowcount()
    linhasDeletadas = cursor.rowcount

    conexao.commit()
    cursor.close()
    conexao.close()

    return linhasDeletadas

def randon_biblioteca_id(conexao):
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM biblioteca")
    linhas = cursor.fetchall()