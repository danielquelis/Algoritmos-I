def lerNumero():
    return(int(input("Digite um número inteiro qualquer: ")))

def soma(a,b,c):
    return(a+b+c)

def media(a,b,c):
    return(soma(a,b,c)/3)

def maior(a,b,c):
    if a>b and a>c:
        M=a
    elif b>a and b>c:
        M=b
    elif c>a and c>b:
        M=c
    return(M)

def menor(a,b,c):
    if a<b and a<c:
        m=n1
    elif b<a and b<c:
        m=n2
    elif c<a and c<b:
        m=n3
    return(m)
i='S'
while i=='S':
    o=int(input("Digite a opção desejada: OPÇÃO [1] SOMA // OPÇÃO [2] MÉDIA // OPÇÃO [3] MAIOR Nº // OPÇÃO [4] MENOR Nº: "))
    n1=lerNumero()
    n2=lerNumero()
    n3=lerNumero()

    if o==1:
        print("A soma dos números digitados é: ",(soma(n1,n2,n3)))
    elif o==2:
        print("A média dos números digitados é: ",(media(n1,n2,n3)))
    elif o==3:
        print("O maior número dentre os digitados é: ",(maior(n1,n2,n3)))
    elif o==4:
        print("O menor número dentre os digitados é: ",(menor(n1,n2,n3)))
    i=input("Você deseja continuar? \nDigite [S] se sim ou [N] se quiser parar: ")
