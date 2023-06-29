class Livro:
    def __init__(self, titulo, autor, anoDePublicacao):
        self.titulo = titulo
        self.autor = autor
        self.anoDePublicacao = anoDePublicacao
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def remover_livro(self, livro):
        self.livros.remove(livro)

    def consultar_livros(self):
        return self.livros



class Biblioteca:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco
        self.Biblioteca = []

    def adicionar_biblioteca(self, biblioteca):
        self.livros.append(biblioteca)

    def remover_biblioteca(self, biblioteca):
        self.livros.remove(biblioteca)

    def consultar_biblioteca(self):
        return self.biblioteca
