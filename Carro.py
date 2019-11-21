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

    def exibirCarro(self):
        return "Carro: {} {}  |  Ano: {}  |  Cor: {}   |   Chassis: {}".format(c1.marca, c1.modelo, c1.ano, c1.cor, c1.chassis)


