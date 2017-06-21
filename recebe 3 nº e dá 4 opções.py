#Programa lê 3 números inseridos pelo usuário e retorna 4 opções de operação.
n1=int(input("Digite o primeiro número: "))
n2=int(input("Digite o segundo número: "))
n3=int(input("Digite o terceiro número: "))
op=int(input("Selecione uma das opções =  Soma  [1] -  Maior  [2] -  Menor  [3] -  Media  [4]"))
r=(n1+n2+n3)
med=r/3

if n1>n2 and n1>n3:
    M=n1
if n2>n1 and n2>n3:
    M=n2
if n3>n1 and n3>n2:
    M=n3

if n1<n2 and n1<n3:
    m=n1
if n2<n1 and n2<n3:
    m=n2
if n3<n1 and n3<n2:
    m=n3

if op==1:
    print("A soma dos 3 números é: ",r)
if op==2:
    print ("O maior número é: ",M)
if op==3:
    print ("O menor número é: ",m)
if op==4:
    print(" A média é",med)
