temp = float(input("IFORME A TEMPERATURA EM CELSIUS: "))
print("1 - Celsius para Fahrenheit")
print("2 - Celsius para Kelvin")
opcao = int(input("Escolha uma opção: "))

Fahrenheit = (temp * 9 / 5) + 32
Kelvin = temp + 273.15 
 
if opcao ==1:
    print(f"{Fahrenheit} °F")
elif opcao ==2:
    print(f"{Kelvin} K")
else:
    print("ERRO!")