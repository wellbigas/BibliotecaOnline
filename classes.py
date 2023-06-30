class Livro:
    def __init__(self, titulo, autor, anoDePublicacao):
        self.titulo = titulo
        self.autor = autor
        self.anoDePublicacao = anoDePublicacao

    def __init__(self, id, titulo, autor, anoDePublicacao, idBiblioteca):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.anoDePublicacao = anoDePublicacao
        self.biblioteca_id = idBiblioteca


class Biblioteca:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def remover_livro(self, livro):
        self.livros.remove(livro)

    def consultar_livros(self):
        return self.livros
