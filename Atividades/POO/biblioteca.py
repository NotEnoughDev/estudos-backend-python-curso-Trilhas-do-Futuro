from datetime import datetime, timedelta

class ItemBiblioteca:
    def __init__(self, nome, autor, edicao, categoria, tipo):
        self.nome = nome
        self.autor = autor 
        self.edicao = edicao
        self.categoria = categoria
        self.tipo = tipo
        self.data_devolucao= None

    def emprestar(self, dias=7):
        self.data_devolucao= datetime.now() + timedelta(days=dias)

    def devolver(self):
        self.data_Devolucao- None

    def esta_emprestado(self):
        return self.data_devolucao is not None

    def descricao(self):
        return f"{self.nome} ({self.categoria}) - {self.autor}, edição: {self.edicao}"

class Livro(ItemBiblioteca):
    def __init__(self, nome, autor, edicao):
        super().__init__(nome, autor, edicao, "Livro")

    def descricao(self):
        return f"📙Livro: {self.nome}\n👨🏽Autor: {self.autor}\nEdição: {self.edicao}\nCategoria: {self.categoria}" 
    
class Manga(ItemBiblioteca):
    def __init__(self, nome, autor, edicao):
        super().__init__(nome, autor, edicao, "Manga")

    def descricao(self):
        return f"📙Manga: {self.nome}\n👨🏽Autor: {self.autor}\nEdição: {self.edicao}\nCategoria: {self.categoria}" 
    
class Comic(ItemBiblioteca):
    def __init__(self, nome, autor, edicao):
        super().__init__(nome, autor, edicao, "Comic")

    def descricao(self):
        return f"📙Comic: {self.nome}\n👨🏽Autor: {self.autor}\nEdição: {self.edicao}\nCategoria: {self.categoria}" 

class BibliotecaModel:
    def __init__(self):
        self.itens_disponiveis = []
        self.itens_emprestados = []
    
    def adicionar_item(self, categoria, nome, autor, edicao):
        if categoria == "Livro":
            novo_item = Livro(nome, autor, edicao)
        elif categoria == "Manga":
            novo_item = Manga(nome, autor, edicao)
        elif categoria == "Comic":
            novo_item = Comic(nome, autor, edicao)
        else:
            raise ValueError ("Categoria inválida")

        self.itens_disponiveis.append(novo_item)

    def listar_disponiveis(self):
        return self.itens_disponiveis
    
    def listar_emprestados(self):
        return self.itens_emprestados

    def remover_item(self, indice):
        if 0<= indice <len(self.itens_disponiveis):
            self.itens_disponiveis.pop (indice)

    def emprestar_item(self, indice, dias=7):
        if 0<= indice <len(self.itens_disponiveis.pop):
            item = self.itens_disponiveis(indice)
            item.emprestar(dias)
            self.itens_emprestados.append(item)

    def devolver_item(self, indice, dias=7):
        if 0<= indice <len(self.itens_emprestados.pop):
            item = self.itens_emprestados(indice)
            item.devolver()
            self.itens_emprestados.append(item)

class UsuarioModel:
    def __init__(self):
        self.usuario = 'admin'
        self.senha = '1234'

    def autenticar(self, usuario, senha):
        return usuario== self.usuario and senha == self.senha