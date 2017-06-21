#Programa lê kilometragem percorrida e volume de combustível inserido e retorna o consumo do veículo
km=int(input("Digite a kilometragem percorrida: "))
l=int(input("Digite o volume de gasolina consumido: "))
c=km/l
print("O seu carro consome %2.2fKm/litro"%c)
