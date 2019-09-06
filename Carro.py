class Veiculo(object):
    def __init__(self, chassis):
        self.chassis = chassis

class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor

    @property
    def getMarca(self):
        return self.marca

    def setMarca(self, marca):
        self.marca = marca

    @property
    def getModelo(self):
        return self.modelo

    def setModelo(self, modelo):
        self.modelo = modelo

    @property
    def getAno(self):
        return self.ano

    def setAno(self, ano):
        self.ano = ano

    @property
    def getCor(self):
        return self.cor

    def setCor(self, cor):
        self.cor = cor


c1 = Carro("Ford", "Ranger", 2019, "Branco")
c1.marca = input("DIGITE O NOME DA MARCA: ")
c1.modelo = input("DIGITE O NOME DA MODELO: ")
c1.ano = input("DIGITE O NOME DA ANO: ")
c1.cor = input("DIGITE O NOME DA COR: ")
print(c1.marca, c1.modelo, c1.ano, c1.cor)
