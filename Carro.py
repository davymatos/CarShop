from Veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, cor, chassis):
        super(Carro, self).__init__(marca, modelo, ano, cor, chassis)
        self.listaCar = []

    #@property
    def getCarro(self):
        return self.listaCar

    def setCarro(self):
        self.listaCar.append(c1.getCarro())
        self.listaCar.append(c1.getModelo())
        self.listaCar.append(c1.getAno())
        self.listaCar.append(c1.getCor())
        self.listaCar.append(c1.getChassis())



c1 = Carro(" ", " ", " ", " ", " ")
c1.setMarca(c1.marca)
c1.setModelo(c1.modelo)
c1.setAno(c1.ano)
c1.setCor(c1.cor)
c1.setChassis(c1.chassis)

print("Carro: {} {}  |  Ano: {}  |  Cor: {}   |   Chassis: {}".format(c1.marca, c1.modelo, c1.ano, c1.cor, c1.chassis))
print(c1.getCarro())


'''
listaCar = []
carros = []

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
'''