class Veiculo:
    def __init__(self, categoria, marca, modelo, ano):
        self.categoria = categoria
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def ligar_carro(self):
        print(f"\nO(A) {self.marca} {self.modelo} está ligado!")

    def descricao(self):
        print("\t\n=== Descrição ===")
        print("==="*15)
        print(f"\nCategoria: {self.categoria}")
        print(f"Nome = {self.marca} {self.modelo}")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.ano}")
        print("==="*15)

class Moto(Veiculo):
    def __init__(self, categoria, marca, modelo, ano):
        super().__init__(categoria, marca, modelo, ano)

    def ligar_moto(self):
        print(f"\nO(A) {self.marca} {self.modelo} está ligado!")


    def descricao(self):
        print("\t\n=== Descrição da Moto ===")
        print("==="*15)
        print(f"\nCategoria: {self.categoria}")
        print(f"Nome = {self.marca} {self.modelo}")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.ano}")
        print("==="*15)

class Carro(Veiculo):
    def __init__(self, categoria, marca, modelo, ano):
        super().__init__(categoria, marca, modelo, ano)

    def ligar_carro(self):
        print(f"\nO(A) {self.marca} {self.modelo} está ligado!")

    def descricao(self):
        print("\t\n=== Descrição do Carro ===")
        print("==="*15)
        print(f"\nCategoria: {self.categoria}")
        print(f"Nome = {self.marca} {self.modelo}")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.ano}")
        print("==="*15)

meu_carro = Carro("SUV compacto", "Hyundai", "Creta", "2022")
meu_carro.ligar_carro()
meu_carro.descricao()

minha_moto = Moto("Street", "Yamaha", "Fazer 250 ABS", "2023")
minha_moto.ligar_carro()
minha_moto.descricao()


