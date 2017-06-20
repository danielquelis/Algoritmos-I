data = input("Informe a data de nascimento [dd/mm/aaaa] -> ")
# print(len(data))
d = int(data[0:2])
m = int(data[3:5])
a = int(data[6:10])
ma = 3
da = 15
i = (2017 - a)
if ma < m:
    print(i - 1)
else:
    if da >= d:
        print(i)
    else:
        print(i - 1)