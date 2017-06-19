n=0
maior=0
menor=0
x=0
while x<10:
    n=int(input("entre com número: "))
    x=x+1
    if n>maior:
        maior=n
    elif n<menor:
        menor=n
print("o maior número é: ",maior)
print("o menor número é: ",menor)