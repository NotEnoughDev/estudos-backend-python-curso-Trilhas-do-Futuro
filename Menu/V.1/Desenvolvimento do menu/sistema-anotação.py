import os
import time

# Função que adiciona uma anotação no arquivo
def adicionar_anotacao(anotacao, arquivo="anotacoes.py"):
    with open(arquivo, "a") as f:
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"# Anotação feita em {timestamp}: {anotacao}\n")
        f.write(f"# {anotacao}\n\n")

def menu():
    print("=== Sistema de Anotações ===")
    print("1 - Adicionar anotação")
    print("2 - Ver anotacoes")
    print("3 - Sair")

def ver_anotacoes(arquivo="anotacoes.py"):
    if os.path.exists(arquivo):
        with open(arquivo, "r") as f:
            conteudo = f.read()
            if conteudo:
                print("\n--- Anotações ---")
                print(conteudo)
            else:
                print("Ainda não há anotações.")
    else:
        print("Arquivo de anotações não encontrado.")

def main():
    while True:
        menu()
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            anotacao = input("Digite sua anotação: ")
            adicionar_anotacao(anotacao)
            print("Anotação adicionada com sucesso!\n")
        elif escolha == "2":
            ver_anotacoes()
        elif escolha == "3":
            print("Saindo do sistema de anotações...")
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()
