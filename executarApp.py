from flask import Flask, render_template, request, redirect
import psycopg2

# importações das classes usadas
from classes import Biblioteca, Livro

# importação de inserção no banco de dados
from manipularBancoDeDados import inserir_no_banco_biblioteca, inserir_no_banco_livro, consultar_bibliotecas, \
    consultar_livros

# importação de conexão banco de dados
from dbConection import get_db_connection

app = Flask(__name__)

biblioteca = Biblioteca("Biblioteca Central",
                        "Rua Principal, 123")  ## ver com will como fazer para assim que adicionar um livro ele referenciar ao id da biblioteca


@app.route('/')
def index():
    connection = get_db_connection();
    bibliotecas = consultar_bibliotecas(connection);
    livros = consultar_livros(connection);
    return render_template('new_index.html', bibliotecas=bibliotecas, livros=livros)


@app.route('/adicionar_livro', methods=['GET', 'POST'])
def adicionar_livro():
    if request.method == 'POST':
        titulo = request.form['titulo']
        autor = request.form['autor']
        ano = int(request.form['ano'])
        livro = Livro(titulo, autor, ano)
        biblioteca.adicionar_livro(livro)
        connection = get_db_connection()
        inserir_no_banco_livro(connection, titulo, autor, ano)
        return redirect('/')
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
        return redirect('/')
    return render_template('adicionar_biblioteca.html')

@app.route('/deletar_livro/<id>', methods=['POST'])
def deletar_livro(id):
    connection = get_db_connection()
    deletar_livro(connection, id)
    connection.close()
    return redirect('/')





if __name__ == '__main__':
    app.run(debug=True)
