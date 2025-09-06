print ("Olá Mundo\n")

def mostrar_menu():
    print("\n--- Estoque ---")
    for produto in estoque:
        print(f"{produto['nome']} - {produto['quantidade']} un. - R$ {produto['preco']:.2f}")
    else:
        print("\nMenu Vazio")

estoque = []

def adicionar_produto():
    nome = input("\nNome do produto: ")
    preco = float(input("Preço do produto: "))
    quantidade = int(input("Quantidade em estoque: "))
    produto = {"nome": nome, "preco": preco, "quantidade": quantidade}
    estoque.append(produto)
    print(f"Produto '{nome}' adicionado com sucesso!")
    print("---------------------------------------")

def ver_estoque():
    if not estoque:
        print("---------------------------------------")
        print("\nEstoque vazio.")
        print("\n---------------------------------------")
    else:
        print("\n--- Estoque ---")
        for produto in estoque:
            print(f"{produto['nome']} - {produto['quantidade']} un. - R$ {produto['preco']:.2f}")
        print("---------------------------------------")
        
def comprar_produto():
        nome = input("\nNome do Produto: ")
        quantidade = int(input("Quantidade do Produto que deseja comprar: "))
        for produto in estoque:
            if produto['nome'].lower() == nome.lower():
                if produto['quantidade'] >= quantidade:
                    total = produto['preco'] * quantidade
                    produto['quantidade'] -= quantidade
                    print(f"Venda realizada: {quantidade} x {produto['nome']} = R$ {total:.2f}")
                    print("---------------------------------------")
                    return
                else:
                    print("Estoque insuficiente.")
                    return
        print("Produto não encontrado.")

def init_menu():
    while True:
        print("\nAntes de entrar na padaria, escolha o seu cargo:")
        print("\n--- Opções ---")
        print("1. Funcionario")
        print("2. Cliente")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            funcionario_menu()
        elif opcao == '2':
            cliente_menu()
        elif opcao == '3':
            print ("Saindo..........")
        else:
            print ("Opção Invalida")
            
def funcionario_menu():
    while True:
        ("\n=== Padaria ===")
        print("\n=== Padaria ===")
        print("\n--- Opções ---")
        print("1. Mostrar Menu")
        print("2. Verificar estoque")
        print("3. Add. Item ao estoque")
        print("4. Sair")
        opcao = input("\nEscolha sua opção: ")
        if opcao == '1':
            mostrar_menu()
        elif opcao ==  '2':
            ver_estoque()
        elif opcao == '3':
            adicionar_produto()
        elif opcao =='4':
           break
            
def cliente_menu():
    while True:
        print("\n=== Padaria ===")
        print("\n--- Opções ---")
        print("1. Mostrar Menu")
        print("2. Realizar Compras")
        print("3. Sair")
        opcao = input("\nEscolha sua opção: ")
        if opcao == '1':
            mostrar_menu()
        if opcao == '2':
            comprar_produto()
        if opcao == '3':
            break    
init_menu()
        
