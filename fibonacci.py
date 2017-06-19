fn=int(input("Digite um numero para saber a sequencia fibonacci : "))
f1=1
f2=1
f=1
i=1
print(f1)
for  i in range (fn):
    if f<=fn:
        print(f)
        f=f1+f2
        f1=f2
        f2=f
