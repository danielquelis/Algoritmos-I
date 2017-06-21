#Programa lê ano de nascimento e retorna se usuário é maior de idade ou não.
a=2017
a1=int(input("Digite o ano do seu nascimento: "))
i=a-a1
if i<18:
    print('MENOR DE IDADE')
else:
    print('MAIOR DE IDADE')
