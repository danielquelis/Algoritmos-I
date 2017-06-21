#Programa lê base e altura do quadrilátero e retorna o valor da área, identificando se é quadrado ou não.
b = int(input("Digite a base do Quadrilátero: "))
h = int(input("Digite a altura do Quadrilátero: "))
a = int(b * h)
if b == h:
    print("A área do quadrado é: %d" % a)
else:
    print("A área do retângulo é: %d" % a)
