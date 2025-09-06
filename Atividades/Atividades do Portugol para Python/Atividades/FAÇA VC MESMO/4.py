numero1=float(input("DIGITE O PRIMEIRO NÚMERO: "))
numero2=float(input("DIGITE O SEGUNDO NÚMERO: "))

opcao = 0
    
while opcao !=5:
    print("------CALCULADORA------")
    print("1-somar")
    print("2-subtrair")
    print("3-multiplicar")
    print("4-dividir")
    print("5-Sair")
    
    opcao=int(input("DIGITE QUAL A OPÇÃO: "))
    
    soma = numero1+numero2
    subtracao = numero1 - numero2
    multplicacao = numero1 * numero2
    divisao = numero1 / numero2
    
    if opcao==1:
        print("Você escolheu somar.")
        print(f"O resultado é: {soma}")
    elif opcao==2:
        print("Você escolheu subtrair.")
        print(f"O resultado é: {subtracao}")
    elif opcao==3:
        print("Você escolheu multiplicar.")
        print(f"O resultado é: {multplicacao}")
    elif opcao==4:
        print("Você escolheu dividir.")
        print(f"O resultado é: {divisao}")
    elif opcao==5:
        print("Saindo...")
    else:
        print("ERRO!")