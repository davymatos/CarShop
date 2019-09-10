class Veiculo(object):
    def __init__(self, carro):
        self.carro = carro

class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.listaCar = []

    @property
    def getMarca(self):
        return self.marca

    def setMarca(self, marca):
        self.marca = input("DIGITE O NOME DA MARCA: ")

    @property
    def getModelo(self):
        return self.modelo

    def setModelo(self, modelo):
        self.modelo = input("DIGITE O NOME DA MODELO: ")

    @property
    def getAno(self):
        return self.ano

    def setAno(self, ano):
        self.ano = input("DIGITE O NOME DA ANO: ")

    @property
    def getCor(self):
        return self.cor

    def setCor(self, cor):
        self.cor = input("DIGITE O NOME DA COR: ")

    @property
    def getCarro(self):
        return self.listaCar.append(Carro(c1.marca, c1.modelo, c1.ano, c1.cor))


c1 = Carro(" ", " ", " ", " ")
c1.setMarca(c1.marca)
c1.setModelo(c1.modelo)
c1.setAno(c1.ano)
c1.setCor(c1.cor)
print("{} {} {} {}".format(c1.marca, c1.modelo, c1.ano, c1.cor))

listaCar = []

print(listaCar)