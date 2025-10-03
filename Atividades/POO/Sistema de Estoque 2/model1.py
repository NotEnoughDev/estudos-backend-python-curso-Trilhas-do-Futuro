import json
import os

class ProdutoModel:
    """Modelo que representa um produto"""
    def __init__(self, id_produto, nome, categoria, quantidade, preco_compra, preco_venda, fornecedor):
        self.id = id_produto
        self.nome = nome
        self.categoria = categoria
        self.quantidade = quantidade
        self.preco_compra = preco_compra
        self.preco_venda = preco_venda
        self.fornecedor = fornecedor
    
    def to_dict(self):
        """Converte o produto para dicionário"""
        return {
            'id': self.id,
            'nome': self.nome,
            'categoria': self.categoria,
            'quantidade': self.quantidade,
            'preco_compra': self.preco_compra,
            'preco_venda': self.preco_venda,
            'fornecedor': self.fornecedor
        }
    
    @staticmethod
    def from_dict(data):
        """Cria um produto a partir de um dicionário"""
        return ProdutoModel(
            data['id'],
            data['nome'],
            data['categoria'],
            data['quantidade'],
            data['preco_compra'],
            data['preco_venda'],
            data['fornecedor']
        )


class EstoqueModel:
    """Modelo que gerencia a coleção de produtos"""
    def __init__(self, arquivo='produtos_estoque.json'):
        self.arquivo = arquivo
        self.produtos = []
        self.carregar_produtos()
    
    def carregar_produtos(self):
        """Carrega produtos do arquivo JSON"""
        if os.path.exists(self.arquivo):
            try:
                with open(self.arquivo, 'r', encoding='utf-8') as f:
                    dados = json.load(f)
                    self.produtos = [ProdutoModel.from_dict(d) for d in dados]
            except Exception as e:
                print(f"Erro ao carregar produtos: {e}")
                self.produtos = []
        else:
            self.produtos = []
    
    def salvar_produtos(self):
        """Salva produtos no arquivo JSON"""
        try:
            with open(self.arquivo, 'w', encoding='utf-8') as f:
                dados = [p.to_dict() for p in self.produtos]
                json.dump(dados, f, ensure_ascii=False, indent=4)
        except Exception as e:
            raise Exception(f"Erro ao salvar produtos: {e}")
    
    def adicionar_produto(self, produto):
        """Adiciona um produto ao estoque"""
        if self.produto_existe(produto.id):
            raise ValueError(f"Já existe um produto com ID {produto.id}")
        self.produtos.append(produto)
        self.salvar_produtos()
    
    def remover_produto(self, id_produto):
        """Remove um produto do estoque"""
        # Converter id_produto para string para garantir comparação correta
        id_produto = str(id_produto)
        
        produto_encontrado = False
        for produto in self.produtos:
            if str(produto.id) == id_produto:
                produto_encontrado = True
                break
        
        if not produto_encontrado:
            raise ValueError(f"Produto com ID {id_produto} não encontrado")
        
        self.produtos = [p for p in self.produtos if str(p.id) != id_produto]
        self.salvar_produtos()
    
    def produto_existe(self, id_produto):
        """Verifica se um produto existe"""
        return any(str(p.id) == str(id_produto) for p in self.produtos)
    
    def obter_todos_produtos(self):
        """Retorna todos os produtos"""
        return self.produtos
    
    def buscar_produto_por_id(self, id_produto):
        """Busca um produto por ID"""
        id_produto = str(id_produto)
        for produto in self.produtos:
            if str(produto.id) == id_produto:
                return produto
        return None
    
    def obter_total_produtos(self):
        """Retorna o total de produtos cadastrados"""
        return len(self.produtos)
    
    def obter_valor_total_estoque(self):
        """Calcula o valor total do estoque"""
        total = sum(p.preco_compra * p.quantidade for p in self.produtos)
        return total

