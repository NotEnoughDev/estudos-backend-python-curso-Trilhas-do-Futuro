import random
numero_secreto = random.randint(1,10)
tentativas =0
contagem_tentativas =0
numero=0
print("Bem vindo ao jogo do Número secreto")
print("Tente advinhar o número secreto 1 e 10")

while tentativas != numero_secreto:
    numero = int(input("\nDigite um numero: "))
    contagem_tentativas= contagem_tentativas+1
    if numero == numero_secreto:
        print("\nVocê Adivinhou o número!")
        print(f"Você precisou de {contagem_tentativas} tentativas")
        break
    elif numero < numero_secreto:
        print ("O número secreto é maior.")
    else:
        print("O número secreto é menor.")