#Programa exibe login randômico, lê senha e libera acesso se acertar
from random import randint
login=[['joao','maria','jose'],['john','mary','joseph']]
x=randint(0,2)
i=1
t=0
while i<=3:
    senha=(input('Para acessar digite a senha do login %s: '%(login[0][x])))
    if senha==(login[1][x]):
        print("Acesso permitido")
        break
    else:
        i=i+1
        t=4-i
        print('Acesso Negado \nVocê tem mais %d tenativas(s)'%t)
        if t==0:
            print('Você foi bloqueado\nTente novamente mais tarde')
