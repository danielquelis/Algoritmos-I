#print("Hello World!!")
'''
data = input("Informe a data de nascimento [dd/mm/aaaa] -> ")
# print(len(data))
d = int(data[0:2])
m = int(data[3:5])
a = int(data[6:10])
ma = 3
da = 15
i = (2017 - a)
if ma < m:
    print(i - 1)
else:
    if da >= d:
        print(i)
    else:
        print(i - 1)
==============================================
i = int(input("Digite sua idade: "))
if i >= 18:
    sit = "adulto"
elif i >= 14:
    sit = "juvenil B"
elif i >= 11:
    sit = "juvenil A"
elif i >= 8:
    sit = "infantil B"
elif i >= 5:
    sit = "infantil A"
print("Sua categoria é: %s" % (sit))
=====================================
n = int(input("Digite um número: "))
print(n - 1)
=====================================================
b = int(input("Digite a base do Quadrilátero: "))
h = int(input("Digite a altura do Quadrilátero: "))
a = int(b * h)
if b == h:
    print("A área do quadrado é: %d" % a)
else:
    print("A área do retângulo é: %d" % a)
=======================================================
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

#tentativa de quicksort
def partition(list, start, end):
    pivot=list[end]
    bottom=start-1
    top=end
    done=0
    while not done:
        bottom=bottom+1
        if bottom==top:
            done=1
            break
        if list[bottom]>pivot:
            list[top]=list[bottom]
            break
    while not done:
        top==top-1
        if top==bottom:
            done=1
            break
    list[top]=pivot
    return top
def quicksort(list, start, end):
    if start<end:
        split=partition(list, start, end)
        quicksort(list, start, split-1)
        quicksort(list, split+1, end)
    else:
        return
    if __name__=="__main__":
        import sys
        list=map(int, sys.argv[1:])
        start=0
        end=len(list)-1
        quicksort(list, start, end)
        print ' '.join(map(str, list))
'''
def quicksort(V):
    if len(V)<=1:
        return V
    pivot=[0]
    equal=[x for x in V if x == pivot]
    lesser=[x for x in V if x < pivot]
    greater=[x for x in V if x > pivot]
    return quicksort(lesser) + equal + quicksort(greater)