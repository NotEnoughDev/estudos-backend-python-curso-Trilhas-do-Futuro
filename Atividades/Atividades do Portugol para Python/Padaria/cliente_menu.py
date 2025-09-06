class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

class Padaria:
    def __init__(self):
        self.estoque = {}
        self.vendas = []

    def adicionar_produto(self, produto):
        self.estoque[produto.nome] = produto
        print(f"'{produto.nome}' adicionado ao estoque.")

    def remover_produto(self, nome_produto, quantidade):
        if nome_produto in self.estoque and self.estoque[nome_produto].estoque >= quantidade:
            self.estoque[nome_produto].estoque -= quantidade
            print(f"{quantidade} unidades de '{nome_produto}' removidas do estoque.")
        elif nome_produto not in self.estoque:
            print(f"Erro: O produto '{nome_produto}' não está no estoque.")
        else:
            print(f"Erro: Estoque insuficiente de '{nome_produto}'. Temos apenas {self.estoque[nome_produto].estoque} unidades.")

    def verificar_estoque(self, nome_produto=None):
        if nome_produto:
            if nome_produto in self.estoque:
                print(f"Estoque de '{nome_produto}': {self.estoque[nome_produto].estoque} unidades.")
            else:
                print(f"Erro: O produto '{nome_produto}' não está no estoque.")
        else:
            print("\n--- Estoque Atual ---")
            for nome, produto in self.estoque.items():
                print(f"{nome}: {produto.estoque} unidades - R$ {produto.preco:.2f}")
            print("----------------------")

    def registrar_venda(self, carrinho):
        total_venda = 0
        itens_vendidos = []
        for nome_produto, quantidade in carrinho.items():
            if nome_produto in self.estoque and self.estoque[nome_produto].estoque >= quantidade:
                preco_unitario = self.estoque[nome_produto].preco
                total_item = preco_unitario * quantidade
                total_venda += total_item
                self.estoque[nome_produto].estoque -= quantidade
                itens_vendidos.append((nome_produto, quantidade, preco_unitario, total_item))
            elif nome_produto not in self.estoque:
                print(f"Erro: Produto '{nome_produto}' não encontrado no estoque.")
                return None
            else:
                print(f"Erro: Estoque insuficiente de '{nome_produto}'.")
                return None

        if itens_vendidos:
            venda = {"itens": itens_vendidos, "total": total_venda}
            self.vendas.append(venda)
            self.imprimir_recibo(venda)
            return venda
        return None

    def imprimir_recibo(self, venda):
        print("\n--- Recibo de Venda ---")
        for item in venda["itens"]:
            nome, quantidade, preco, total = item
            print(f"{nome} x {quantidade} - R$ {preco:.2f} = R$ {total:.2f}")
        print(f"-----------------------")
        print(f"Total: R$ {venda['total']:.2f}")
        print("-----------------------")
        print("Obrigado pela sua compra!")

    def mostrar_menu(self):
        print("\n--- Menu de Produtos ---")
        for nome, produto in self.estoque.items():
            print(f"{nome} - R$ {produto.preco:.2f}")
        print("------------------------")

def main():
    padaria = Padaria()

    # Adicionando alguns produtos iniciais
    padaria.adicionar_produto(Produto("Pão Francês", 0.50, 100))
    padaria.adicionar_produto(Produto("Pão Doce", 0.20, 50))
    padaria.adicionar_produto(Produto("Bolo de Cenoura", 10.00, 20))
    padaria.adicionar_produto(Produto("Café Expresso", 3.50, 30))

def cliente_menu():
    while True:
        print("\n=== Padaria ===")
        print("\n--- Opções ---")
        print("1. Mostrar Menu")
        print("2. Realizar Compras")
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            padaria.mostrar_menu()
        if opcao == '2':
            print("2")
        if opcao == '3':
            print("3")
            break

cliente_menu()