vendedor =input("NOME DO VENDEDOR: ")
salario =float (input("SALÁRIO: "))
quantvendas=int(input("QUANTIDADE DE VENDAS: "))
bonus = 0.15*salario
pagamento = bonus+salario

if quantvendas >= 20:
    print("===RESUMO==")
    print(f"Nome do vendedor: {vendedor}")
    print(f"Salário: {salario:.2f}")
    print(f"Meta alcançada!")
    print(f"Valor do bônus: {bonus:.2f}")
    print(f"Salário final: {pagamento:.2f}")
        
else:
    print("META NÃO ATINGIDA.")
