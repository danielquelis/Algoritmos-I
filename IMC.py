peso = float(input("Diga qual o seu peso: "))
altura = float(input("Diga qual a sua altura: "))
genero = input("Qual o seu genero ?(M/F): ")
imc = peso/(altura*altura)
sit = ''
if genero == "F" or genero == "f":
    if (imc < 19):
        sit = "abaixo do peso ideal"
    elif (imc <= 23.9):
        sit = "com peso ideal"
    elif (imc <= 28.9):
        sit = "com grau leve de obesidade"
    elif (imc <= 38.9):
        sit = "com grau moderado de obesidade"
    elif (imc >= 39):
        sit = "com grau de obesidade mórbida"
else:
    if (imc < 20):
        sit = "abaixo do peso ideal"
    elif (imc <= 24.9):
        sit = " com peso ideal"
    elif (imc <= 29.9):
        sit = "com grau leve de obesidade"
    elif (imc <= 39.9):
        sit = "com grau moderado de obesidade"
    elif (imc > 39.9):
        sit = "com grau de obesidade mórbida"
print("Seu imc é: %2.1f"%imc)
print("Você está %s"%sit)