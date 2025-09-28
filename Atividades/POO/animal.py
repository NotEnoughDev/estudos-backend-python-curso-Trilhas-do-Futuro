class Animal:
    def __init__(self, nome, especie, idade):
        self.nome = nome
        self.especie = especie
        self.idade = idade

    def fazer_som(self, som):
        print(f"{self.nome} faz {som}!")

    def aniversario(self):
        self.idade += 1
        print(f"{self.nome} agora tem {self.idade} anos!")


class Cachorro(Animal):
    def __init__(self, nome, idade):
        super().__init__(nome, "Cachorro", idade)

    def latir(self):
        self.fazer_som("au au")


class Gato(Animal):
    def __init__(self, nome, idade):
        super().__init__(nome, "Gato", idade)

    def miar(self):
        self.fazer_som("miau")


dog = Cachorro("Rex", 3)
cat = Gato("Mimi", 2)

dog.latir()
cat.miar()

dog.aniversario()
cat.aniversario()
