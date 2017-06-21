#Programa lê ano inserido por usuário e retorna se bissexto ou não.
a=int(input("Digite o ano que você quer consultar: "))
i='s'
while i=='s':
    if a%4==0 and a%100!=0 or a%400==0:
        print("O ano %s é bissexto"%a)
    else:
        print("O ano %s não é bissexto"%a)
    i=input("Deseja continuar? \nDigite [s] se sim ou [n] para não: ")
    a=int(input("Digite o ano que você quer consultar: "))
print("Programa encerrado")
