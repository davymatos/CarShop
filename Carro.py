class Veiculo(object):
    def __init__(self, chassis):
        self.chassis = chassis

class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor

c1 = Carro("Ford", "Ranger", 2019, "Branco")
print("{} {} {} {}".format(c1.marca, c1.modelo, c1.ano, c1.cor))
print(c1.marca, c1.modelo, c1.ano, c1.cor)
