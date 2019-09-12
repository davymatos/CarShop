class Veiculo(object):
    def __init__(self, chassis):
        self.chassis = chassis

    @property
    def getChassis(self):
        return self.chassis

    def setChassis(self, chassis):
        self.chassis = input("DIGITE O NOME DA CHASSIS: ")

class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, cor, chassis):
        super(Carro, self).__init__(chassis)
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
        return self.listaCar.append(Carro(c1.marca, c1.modelo, c1.ano, c1.cor, c1.chassis))

    def setCarro(self):
        self.listaCar.append(Carro)

listaCar = []
carros = []

c1 = Carro(" ", " ", " ", " ", " ")
c1.setMarca(c1.marca)
c1.setModelo(c1.modelo)
c1.setAno(c1.ano)
c1.setCor(c1.cor)
c1.setChassis(c1.chassis)

'''
listaCar.append(Carro(c1.marca, c1.modelo, c1.ano, c1.cor, c1.chassis))

for j in listaCar:
    print(listaCar[0])
    print(listaCar[1])
    print(listaCar[2])
    print(listaCar[3])
    print(listaCar[4])
'''

listaCar.append(c1.getMarca)
listaCar.append(c1.getModelo)
listaCar.append(c1.getAno)
listaCar.append(c1.getCor)
listaCar.append(c1.getChassis)

carros.append(listaCar)

for i in carros:
    print("Marca: ", i[0])
    print("Modelo: ", i[1])
    print("Ano: ", i[2])
    print("Cor: ", i[3])
    print("Chassis: ", i[4])
