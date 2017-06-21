#Programa lê data de nascimento do usuário, insere num vetor e calcula a idade baseado na data atual.
data = input("Informe a data de nascimento [dd/mm/aaaa] -> ")
d = int(data[0:2])
m = int(data[3:5])
a = int(data[6:10])
ma = 6
da = 21
i = (2017 - a)
if ma < m:
    print(i - 1)
else:
    if da >= d:
        print(i)
    else:
        print(i - 1)
