datas="12ago2021,02set2020,20jan2022,11out2019,09mar2020,10dez2022"
lista_datas = datas.split(",")
nova_string = " ".join(lista_datas)

print("String reconstruída:", nova_string)

count = 0
lista = []
for x in lista_datas:
    if "2022" in x:
        lista.append(x)
        count += 1
print("Datas com 2022:", lista)

dias = []

for x in lista_datas:
    dia = x[:2]
    dias.append(dia)

dias.sort()
print("Dias ordenados:", dias)