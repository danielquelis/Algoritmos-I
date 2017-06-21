#Programa lê nome e senha e rejeita quando idênticos.
n=str(input("Digite o seu nome: "))
s=str(input("Digite uma senha diferente do sue nome: "))
while n==s:
    print("Senha inválida. Tente novamente.")
    s=str(input("Digite uma senha diferente do seu nome: "))
print("Seu cadastro foi realizado com sucesso!")
