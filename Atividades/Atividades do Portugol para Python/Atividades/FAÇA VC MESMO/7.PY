nome = input("Insira seu nome: ")
print("=====IMPORTANTE=====")
print("R$90 por dia alugado")
print("R$0,20 por Km rodado")
dias = int(input("Informe quantos dias ficou alugado: "))
km = float(input("Informe quantos quilometros rodados: "))

total = (dias * 90) + (km * 0.20)

import os

def limpa_tela():
    sistema = os.name
    if sistema == 'nt':  # Para Windows
        os.system('cls')
    else:  # Para Linux ou MacOS
        os.system('clear')

# Exemplo de uso
limpa_tela()

print(f"Cliente: {nome}")
print("===============================")
print(f"{dias} Dias")
print(f"{km} Quilômetros")
print("===============================")
print(f"Total a pagar: R${total:.2f}")