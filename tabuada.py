print("Programa de Tabuada de 1 a 10")
n=int(input("Qual tabuada você quer consultar? "))
i=1
while i<=10:
    result=i*n
    print("%d x %d = %d"%(n,i,result))
    i=i+1