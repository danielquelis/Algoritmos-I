n1=int(input('Digite a 1ª nota: '))
n2=int(input('Digite a 2ª nota: '))
m=(n1+n2)/2
print('Sua média é %1.2f'%m)
if m>=9:
    print('Seu conceito é ÓTIMO')
elif m>=7:
    print('Seu conceito é BOM')
elif m>=6:
    print('Seu conceito é SUFICIENTE')
else:
    print('Seu conceito é INSUFICIENTE')
