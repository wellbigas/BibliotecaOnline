class Livro:
    def __init__(self, titulo, autor, anoDePublicacao):
        self.titulo = titulo
        self.autor = autor
        self.anoDePublicacao = anoDePublicacao

    def construir_com_id(self, id, titulo, autor, anoDePublicacao):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.anoDePublicacao = anoDePublicacao


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
