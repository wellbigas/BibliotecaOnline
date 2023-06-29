import datetime
import time

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
    cursor.execute("SELECT nome, endereco FROM biblioteca")
    bibliotecas = cursor.fetchall()
    cursor.close()
    conexao.close()
    return bibliotecas

