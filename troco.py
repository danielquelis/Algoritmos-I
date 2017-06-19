conta=int(input("Digite o valor da conta :  "))
pagamento=int(input("Digite o valor do do pagamento :  "))
troco=pagamento-conta
notas=[50,20,10,5,2,1]
i=0
while troco>0:
	n=troco/notas[i]
	troco=troco%notas[i]
	if int(n) != 0:
		print('%d nota(s) de R$ %.2f' %(n, notas[i]))
	i=i+1
