#Programa lê área a ser pintada e retorna quantas latas serão necessárias e o custo
a=int(input("Digite a área a ser pintada: "))
l=a//54
if a%54!=0:
    l=l+1
    v=l*80
    print("Você precisa de %d latas"%l)
    print("Custa %d reais"%v)
else:
    v=l*80
    print("Você precisa de %d latas"%l)
    print("custa %d reais"%v)
