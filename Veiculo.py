class Veiculo(object):
    def __init__(self, marca, modelo, ano, cor, chassis):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.chassis = chassis

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
    def getChassis(self):
        return self.chassis

    def setChassis(self, chassis):
        self.chassis = input("DIGITE O NOME DA CHASSIS: ")