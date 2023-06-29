import flask
from flask import Flask, render_template, request, redirect
import importlib

importlib.reload(flask)

# importações das classes usadas
from classes import Biblioteca, Livro

# importação de inserção no banco de dados
from manipularBancoDeDados import inserir_no_banco_biblioteca, inserir_no_banco_livro, consultar_bibliotecas

# importação de conexão banco de dados
from dbConection import get_db_connection

app = Flask(__name__)

biblioteca = Biblioteca("Biblioteca Central",
                        "Rua Principal, 123")  ## ver com will como fazer para assim que adicionar um livro ele referenciar ao id da biblioteca


@app.route('/Inicio')
def index():
    return render_template('new_index.html', biblioteca=Biblioteca, livro=Livro)


@app.route('/adicionar_livro', methods=['GET', 'POST'])
def adicionar_livro():
    if request.method == 'POST':
        titulo = request.form['titulo']
        autor = request.form['autor']
        ano = int(request.form['ano'])
        livro = Livro(titulo, autor, ano)
        livro.adicionar_livro(livro)
        connection = get_db_connection()
        inserir_no_banco_livro(connection, titulo, autor, ano)
        return redirect('/Inicio')
    return render_template('adicionar_livro.html')


@app.route('/adicionar_biblioteca', methods=['GET', 'POST'])
def adicionar_biblioteca():
    if request.method == 'POST':
        nome = request.form['nome']
        endereco = request.form['endereco']
        nova_biblioteca = Biblioteca(nome, endereco)
        global biblioteca
        biblioteca = nova_biblioteca
        connection = get_db_connection()
        inserir_no_banco_biblioteca(connection, nome, endereco)
        return redirect('/Inicio')
    return render_template('adicionar_biblioteca.html')


@app.route('/listar_bibliotecas', methods=['GET'])
def listar_bibliotecas():
    connection = get_db_connection()
    cursor = connection.cursor()

    # Executar a consulta SQL utilizando da classe consultar
    cursor.execute(consultar_bibliotecas)

    # Obter os resultados da consulta
    resultados = cursor.fetchall()

    # Iterar pelos resultados e retornar linha a linha
    for linha in resultados:
        primeira_coluna = linha[0]
        segunda_coluna = linha[1]
        terceira_coluna = linha[2]
        # Faça o que desejar com as colunas aqui
        print(f"Primeira coluna: {primeira_coluna}")
        print(f"Segunda coluna: {segunda_coluna}")
        print(f"Terceira coluna: {terceira_coluna}")

    # Fechar o cursor e a conexão com o banco de dados
    cursor.close()
    connection.close()

    return render_template('listar_bibliotecas.html', bibliotecas=resultados)


if __name__ == '__main__':
    app.run(debug=True)
