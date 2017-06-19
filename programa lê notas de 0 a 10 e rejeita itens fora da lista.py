n=int(input("Digite um número de 0 a 10: "))
while n<0 or n>10:
    print("Número inválido")
    n=int(input("Digite um número de 0 a 10: "))
print(n)