c=int(input("Digite o número de cigarros que você fuma por dia: "))
a=int(input("A quantos anos você fuma? "))
tf=c*10*365*a
dp=tf/8760
print("Você perdeu %2.2f dias de vida por causa do cigarro, seu trouxa!"%dp)