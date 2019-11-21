from Carro import Carro
from Veiculo import Veiculo

listaCar = []

c1 = Carro(' ', ' ', ' ', ' ', ' ')
c1.setMarca(c1.marca)
c1.setModelo(c1.modelo)
c1.setAno(c1.ano)
c1.setCor(c1.cor)
c1.setChassis(c1.chassis)

listaCar.append(Carro)
#listaCar.append(c1.modelo)
#listaCar.append(c1.ano)
#listaCar.append(c1.cor)
#listaCar.append(c1.chassis)

print("Carro: {} {}  |  Ano: {}  |  Cor: {}   |   Chassis: {}".format(c1.marca, c1.modelo, c1.ano, c1.cor, c1.chassis))
print(listaCar)
