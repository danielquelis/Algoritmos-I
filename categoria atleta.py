i = int(input("Digite sua idade: "))
if i >= 18:
    sit = "adulto"
elif i >= 14:
    sit = "juvenil B"
elif i >= 11:
    sit = "juvenil A"
elif i >= 8:
    sit = "infantil B"
elif i >= 5:
    sit = "infantil A"
print("Sua categoria é: %s" % (sit))