

print ("Olá Mundo\n")
print ("Seja Bem vindo ao meu 'Menu de Atividades'")
print ("Aqui colocarei as anotações das atividades feitas durante meu curso mais anotações\n")

def main_menu():
#Provavelmente vou usar esse codigo aqui: ##########################
#    import os                                                     #
#    def limpa_tela():                                             #
#        sistema = os.name                                         #
#        if sistema == 'nt':                                       #
#            os.system('cls')                                      #
#        else:                                                  #######  
#            os.system('clear')                                  #####
                                                                  ###
    while True:                                                    #
        print("\n=== Menu Principal ===")         #                
        print("\n--- Opções ---")                ##                #
        print("1. Anotações sobre o Python")    ###                # 
        print("2. Anotações sobre o Portugol") #####################
        print("3. Atividades do Python")        ### 
        print("4. Atividades do Portugol")       ##
        print("5. Sair")                          #
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            notes_menu()
        elif opcao == '2':
            print("2")
        elif opcao == '3':
            python_exercises_menu()
        elif opcao == '4':
            portugol_exercises_menu()
        elif opcao == '5':
            print("Saindo.......")
            print("\nPrograma Finalizado\n")
            break
        else:
            print ("Opção Invalida")
            main_menu()

def notes_menu():
    while True:
        print("\n=== Menu de Anotações do Python ===")
        print("\n--- Opções ---")
        print("1. Notas do Python")
        print("2. Desenvolvimento do Menu Geral")
        print("3. Voltar para o Menu Principal") 
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            print("---------------------------------------")
            print("Olá Mundo")
            print("---------------------------------------")
            print("Anotações sobre o Python")
            print("---------------------------------------")
            print("input = É um comando como o "'Leia (Variavel)'" do portugol onde se escreve na mesma linha que a usa.")
            print("Em outras palavras, um comando para poder dar entrada de dados ou informações ao programa.")
            print("   Exemplo: 'nome= input (Digite seu nome: )'")
            print("   Nesse exemplo, se colocasse isso num programa Python, poderei escrever algo")
            print("\nfloat = Variavel de n° reais")
            print("\nint = Variavel de nº inteiros")
            print("\n'f' = Comando usado para referir uma variavel de maneira mais rapida. Geralmente, quando for referida, usar '{'}'")
            print("\nif = Se")
            print("\nif not = Se não(Caso contrario)")
            print("\nelse = Senão")
            print("\nelif = Senão se")
            print("\nprint = Escreva")
            print("'==' = Igual comparativo")
            print("':' = Substituição das chaves do Portugol ou seja, blocos de comando.")
            print("\n\n Notas de Codigos:")
            print("\n1            import os") #Peguei da Internet ksksks
            print("\n2            def limpa_tela():")
            print("3                sistema = os.name")
            print("4                if sistema == 'nt':          = Basicamente um codigo para limpar o terminal") # Para Windows
            print("5                    os.system('cls')           = A linha 4 é o codigo para Windows quando digitado no Terminal") 
            print("6                else:           = Para Linux ou MacOs, linha 7")  # Para Linux ou MacOS
            print("7                    os.system('clear')")
            print("\nExemplo de uso: ") # Exemplo de uso
            print("limpa_tela() = Com o codigo escrito em seu script, poderá usar esse codigo para ativa-lo")
            print("\n---------------------------------------")
        if opcao == '2':
            print("---------------------------------------")
            print("Por que perder tempo fazendo esse menu?")
            print("\nNa epoca, eu quis me desafiar programando além do que sabia, me forçando a buscar a aprender mais. Esse menu, por exemplo nasceu assim.")
            print("\n\nComo exatamente essa ideia de menu nasceu?")
            print("\nQuando estava aprendendo logica da programação com o Portugol tinha decidido aprender programação com esse mesmo objetivo, se tinha como fazer um menu para mim seria um programa e assim, depois de ser introduzido ao Python, fiz o mesmo.")
            print("\n\nTirei alguma referência? Busquei algum conhecimento?")
            print("\nSim, eu tirei uma referência, no caso, da propria ia da google e sim, busquei me apronfundar para fazer esse menu se tornar realidade. Alias uma curiosidade é de que escrevi isso em 12 de Maio de 2025 as 19:32pm e que nesse tempo, o menu ainda não estava pronto então.... saudações do passado ;)")
            print("\n\n     Olá eu do passado não tão distante, sou do futuro de 16 de maio as 19:31pm e já terminei de fazer a maior parte desse script adicionando:")
            print("\n- Atividades do Python")
            print("\n- Atividades do Portugol")
            print("\nObviamente vou add. muito mais com o passar do tempo e talvez.... sei la, fazer um menu ainda maior; um programa que reuna toda minha evolução com o Python. E sim, usei referências e ate copiei e colei atividades dos outros, mudei algumas coisas para que não ficasse igual e claro, procurei entender os scripts das atividades de outros, estudei e aprimorei do meu proprio jeito. Como já dizia: 'Copía só não faz igual'. Enfim, espero que eu do futuro avançe ainda mais. Alias, Olá Eu do futuro!")
            print("---------------------------------------")
        if opcao == '3':
            break
    main_menu()

def python_exercises_menu():
    while True:
        print("\n=== Menu de Atividades do Python ===")
        print("\n--- Opções ---")
        print("1. Dobro de um Numero")
        print("2. Par ou Impar")
        print("3. Numero Secreto")
        print("4. Soma Acumulativa")
        print("5. Tabuada")
        print("6. Cardapio")
        print("7. Voto")
        print("8. Voltar para o Menu principal")
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            print("\nOlá Mundo!")
            print("---------------------------------------")
            print("Dobro de um Numero")
            print("---------------------------------------")
            numero= int(input("\nDigite um número: "))
            dobro = numero*2
            print (f"O dobro de {numero} é {dobro}")
            print("\n---------------------------------------")
        elif opcao == '2':
            print("\nOlá Mundo!")
            print("---------------------------------------")
            print("Par ou Impar")
            print("---------------------------------------")
            numero= int(input("Digite um número: "))
            if numero %2==0:
                print (f"O número {numero} é par")
                print("\n---------------------------------------")
            else:
                print (f"O número {numero} é impar")
                print("\n---------------------------------------")
        elif opcao == '3':
            print("\nOlá Mundo!")
            print("---------------------------------------")
            print("Numero Secreto")
            print("---------------------------------------")    
            import random
            numero_secreto = random.randint(1,10)
            tentativas =0
            contagem_tentativas =0
            numero=0
            print("Bem vindo ao jogo do Número secreto")
            print("Tente advinhar o número secreto 1 e 10")

            while tentativas != numero_secreto:
                numero = float(input("\nDigite um numero: "))
                contagem_tentativas= contagem_tentativas+1
                if numero == numero_secreto:
                    print("\nVocê Adivinhou o número!")
                    print(f"Você precisou de {contagem_tentativas} tentativas")
                    print("\n---------------------------------------")
                    break
                elif numero < numero_secreto:
                    print ("O número secreto é maior.")
                else:
                    print("O número secreto é menor.")
        elif opcao == '4':
            print("\nOlá Mundo!")
            print("---------------------------------------")
            print("Soma Acumulativo")
            print("---------------------------------------") 
            soma= 0
            numero =1
            while numero !=0:
                numero = int(input("Digite um número (0 para sair): "))
                soma = soma + numero
                if numero!=0:
                    print(f"\nA soma até o momento: {soma} ")
                    print(f"A soma dos números digitados é: {soma}")
                    print("\n---------------------------------------")
        elif opcao == '5':
            print("\nOlá Mundo!")
            print("---------------------------------------")
            print("Tabuada")
            print("---------------------------------------") 
            numero= int(input("Digite um número: "))
            for i in range (11):
                print(f"{numero} x {i} = {numero*i}")
                print("\n---------------------------------------")
        elif opcao == '6':
            print("\nOlá Mundo!")
            print("---------------------------------------")
            print("Cardapio")
            print("---------------------------------------") 
            opcao = 0
            while opcao != 5:
                print("\n=== Cardápio ===")
                print("\n1- Hamburguer")
                print("2- Pizza")
                print("3- Salada")
                print("4- Refrigerante")
                print("5- Sair")
                opcao = int(input("Escolha uma opção: "))
                if opcao == 1:
                    print("\nVocê escolheu hamburguer!")
                    print("---------------------------------------")
                elif opcao == 2:
                    print("\nVocê escolheu pizza!")
                    print("---------------------------------------")
                elif opcao == 3:
                    print("\nVocê escolheu salada!")
                    print("---------------------------------------")
                elif opcao == 4:
                    print("\nVocê escolheu refrigerante!")
                    print("---------------------------------------")
                elif opcao == 5:
                    print("\nSaindo do cardapio..........")
                    print("---------------------------------------")
                    break
                else:
                    print("Opção inválida. Tente novamente!")
                    print("\n---------------------------------------")
        elif opcao == '7':
            print("\nOlá Mundo!")
            print("---------------------------------------")
            print("Voto")
            print("---------------------------------------") 
            ano_atual=2025
            ano_nascimento= int(input("Digite seu ano de nascimento: "))
            idade = ano_atual- ano_nascimento
            print(f"Você tem {idade} anos.")
            if idade <16:
                print("Você não pode votar!")
                print("\n---------------------------------------")
            elif idade <18 or idade >70:
                print("Seu voto é opçional.")
                print("\n---------------------------------------")
            elif idade >=18:
                print("Seu voto é obrigatorio.")
                print("\n---------------------------------------")

        elif opcao == '8':
            break
        else:
            print ("Opção Invalida")

def portugol_exercises_menu():
    while True:
        print("\n=== Menu de Atividades do Portugol ===")
        print("\n--- Opções ---")
        print("1. Padaria")
        print("2. Atividades do 'Faça você mesmo'")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            init_menu()
        if opcao == '2':
            faca_voce_mesmo_menu()
        if opcao == '3':
            break

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
        print("\nOlá Mundo")
        print("---------------------------------------")
        print("Padaria")
        print("---------------------------------------")
        print("Antes de entrar na padaria, escolha o seu cargo:")
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
            break
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
    
def faca_voce_mesmo_menu():
    while True:
        print("\n=== Faça você mesmo ===")
        print("\n--- Opções ---")
        print("1. Autonomia de Carro")
        print("2. Parcelamento de Compras")
        print("3. Calculadora de bonûs por renda")
        print("4. Calculadora Simples")
        print("5. Calculo IMC")
        print("6. Conversor de Temperatura")
        print("7. Locadora de Carro")
        print("8. Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            print("\nOlá Mundo")
            print("---------------------------------------")
            print("Autonomia de Carro")
            print("---------------------------------------")
            distancia = float(input("Digite quantos KM foram percorridos: "))
            litros = float(input("Informe a quantidade de litros que foi colocado: "))

            consumo = distancia/litros

            print(f"A autonomia do carro é: {consumo} km/lt")
            print("---------------------------------------")
        if opcao == '2':
            print("\nOlá Mundo")
            print("---------------------------------------")
            print("Parcelamento de Compras")
            print("---------------------------------------")
            valor= int(input("Valor do Produto: "))
            divisao = int(input("Quantas vezes ser dividido: "))
            valor_da_compra= valor/divisao
            print (f"O valor de cada parcela será: R$ {valor_da_compra} .")
            print("---------------------------------------")
        if opcao == '3':
            print("\nOlá Mundo")
            print("---------------------------------------")
            print("Calculadora de bonûs por renda")
            print("---------------------------------------")
            vendedor =input("Nome: ")
            salario =float (input("Salário: "))
            quantvendas=int(input("Quantidade de Vendas: "))
            bonus = 0.15*salario
            pagamento = bonus+salario

            if quantvendas >= 20:
                print("===RESUMO==")
                print(f"\nNome: {vendedor}")
                print(f"Salário: {salario:.2f}")
                print(f"Valor do bônus: {bonus:.2f}")
                print(f"Total: {pagamento:.2f}")
                print(f"Meta alcançada!")
                print("---------------------------------------")
        
            else:
                print("Meta não atingida!")
                print("---------------------------------------")
        if opcao == '4':
            print("\nOlá Mundo")
            print("---------------------------------------")
            print("Calculadora Simples")
            print("---------------------------------------")
            numero1=float(input("Digite o 1º numero: "))
            numero2=float(input("Digite o 2º numero: "))

            opcao = 0
    
            while opcao !=5:
                print("\n------CALCULADORA------")
                print("1. Soma")
                print("2. Subtração")
                print("3. Multiplicação")
                print("4. Divisão")
                print("5. Sair")
    
                opcao=int(input("Escolha uma opção: "))
    
                soma = numero1+numero2
                subtracao = numero1 - numero2
                multplicacao = numero1 * numero2
                divisao = numero1 / numero2
    
                if opcao==1:
                    print("Você escolheu somar.")
                    print(f"\nO resultado é: {soma}")
                    print("---------------------------------------")
                elif opcao==2:
                    print("Você escolheu subtrair.")
                    print(f"\nO resultado é: {subtracao}")
                    print("---------------------------------------")
                elif opcao==3:
                    print("Você escolheu multiplicar.")
                    print(f"\nO resultado é: {multplicacao}")
                    print("---------------------------------------")
                elif opcao==4:
                    print("Você escolheu dividir.")
                    print(f"\nO resultado é: {divisao}")
                    print("---------------------------------------")
                elif opcao==5:
                    break
                else:
                    print("Erro!")
                    print("---------------------------------------")
        if opcao == '5':
            print("\nOlá Mundo")
            print("---------------------------------------")
            print("Calculo IMC")
            print("---------------------------------------")
            nome = input("Nome: ")
            peso = float(input("Peso: "))
            altura = float(input("Altura: "))

            imc = peso / (altura*altura)

            print("Resultado:")
            if imc < 18.5:
                print("\nVocê está abaixo do peso!")
                print("---------------------------------------")
            elif imc >= 18.5 and imc <= 24.9:
                print("\nClassificação: peso normal!")
                print("---------------------------------------")
            elif imc >= 25.0 and imc <= 29.9:
                print("\nClassificação: sobrepeso!")
                print("---------------------------------------")
            elif imc >=30.0:
                print("\nClassificação: obesidade")
                print("---------------------------------------")

        if opcao == '6':
            print("\nOlá Mundo")
            print("---------------------------------------")
            print("Conversor de Temperatura")
            print("---------------------------------------")
            temp = float(input("Digite o valor da conversão: "))
            print("\n1. Celsius para Fahrenheit")
            print("2. Celsius para Kelvin")
            opcao = int(input("\nEscolha uma opção: "))

            Fahrenheit = (temp * 9 / 5) + 32
            Kelvin = temp + 273.15 
 
            if opcao ==1:
                print(f"O resultado da conversão em Celsium é de: {Fahrenheit} °F")
                print("---------------------------------------")
            elif opcao ==2:
                print(f"O resultado da conversão em Celsium é de: {Kelvin} K")
                print("---------------------------------------")
            else:
                print("Erro!")
                print("---------------------------------------")
        if opcao == '7':
            print("\nOlá Mundo")
            print("---------------------------------------")
            print("Locadora de Carro")
            print("---------------------------------------")
            nome = input("Nome: ")
            print("\n--- Tabela de Preços ---")
            print("R$90 por dia alugado")
            print("R$0,20 por Km rodado")
            dias = int(input("Informe quantos dias ficou alugado: "))
            km = float(input("Informe quantos quilometros rodados: "))

            total = (dias * 90) + (km * 0.20)
            
            import os

            def limpa_tela():
                sistema = os.name
                if sistema == 'nt':  
                    os.system('cls')
                else:  
                    os.system('clear')

            print(f"Cliente: {nome}")
            print("===============================")
            print(f"{dias} Dias")
            print(f"{km} Quilômetros")
            print("===============================")
            print(f"Total a pagar: R${total:.2f}")
            print("===============================")
            print("\n---------------------------------------")
        if opcao == '8':
            break
            
    
main_menu()
        

        
        
        

        
         

