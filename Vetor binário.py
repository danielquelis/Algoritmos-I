#Programa lê valores inseridos num vetor pelo usuário e atribui 0 e 1
# para valores positivos e negativos respectivamente
def binario(vet):
    for i in range(30):
        if vet[i]>0:
            vet[i]=1
        else:
            vet[i]=0
    return(vet);

vet=[]
for i in range(30):
    vet.append(int(input('Digite um valor: ')))
print(vet)
binario(vet)
print(vet)
