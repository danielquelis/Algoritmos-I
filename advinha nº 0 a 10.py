from random import randint
n=randint(0, 10)
n1=int(input("Advinhe qual número estou pensando? "))
t=1
while n1!=n:
    t=t+1
    if n1>n:
        print("O número é menor...")
        n1=int(input("Tente mais uma vez "))
    elif n1<n:
        print("O número é maior...")
        n1=int(input("Tente outra vez "))
print("Acertou!!")
print("Você precisou de %d tentativas para acertar!"%t)
