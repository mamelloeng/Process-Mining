notas=[11.2, 15, 8.7, 17.2, 7.9 ]

notas.append(10.9)
print(notas)
print(len(notas))
print(min(notas))
media = sum(notas) / len(notas)
print("{:.2f}".format(media))