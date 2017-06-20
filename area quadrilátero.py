b = int(input("Digite a base do Quadrilátero: "))
h = int(input("Digite a altura do Quadrilátero: "))
a = int(b * h)
if b == h:
    print("A área do quadrado é: %d" % a)
else:
    print("A área do retângulo é: %d" % a)