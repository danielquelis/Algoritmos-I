nome=[]
idade=[]
i=0
for i in range (10):
    nome.append(input('Digite o seu nome: '))
    idade.append(int(input('Digite sua idade: ')))
    i=i+1
print(nome,idade)