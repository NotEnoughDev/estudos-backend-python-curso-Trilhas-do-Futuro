nome = input("INSIRA SEU NOME: ")
peso = float(input("INSIRA SEU PESO: "))
altura = float(input("INSIRA SUA ALTURA: "))

imc = peso / (altura*altura)

print("===RESULTADO===")
print(F"{nome}")
if imc < 18.5:
    print("Você está abaixo do peso!")

elif imc >= 18.5 and imc <= 24.9:
    print("Classificação: peso normal!")
elif imc >= 25.0 and imc <= 29.9:
    print("Classificação: sobrepeso!")
elif imc >=30.0:
    print("Classificação: obesidade")