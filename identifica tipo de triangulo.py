a=float(input("Digite a base do triangulo: "))
b=float(input("Digite um lado do triangulo: "))
c=float(input("Digite outro lado do triangulo: "))
if a==b and b==c:
    print("Seu triângulo é equilátero")
elif a!=b or b!=c:
    print("Seu triângulo é isósceles")
elif a!=b and b!=c:
    print("Seu triângulo é escaleno")