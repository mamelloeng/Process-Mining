Txt="""Python é uma linguagem de programação
3 de 3
de alto nível, interpretada de script, imperativa, orientada a objetos,
funcional, de tipagem dinâmica e forte."""

print(Txt.upper())

p = input("Introduza uma palavra \n->")

lista_Txt = Txt.split()

if p in lista_Txt:
    print("A palavra {} foi encontrada {} vezes".format(p, lista_Txt.count(p)))
else:
    print("A palavra {} não foi encontrada".format(p))
no = 0
for x in lista_Txt:
    for y in x:
        if y == "o":
            no += 1
print("A letra 'O' aparece {} vezes".format(no))
print(Txt)

np = 0

print(Txt.replace("p" , "_").replace("P", "_"))
''' for x in lista_Txt:
    for y in x:
        if y == "p":
            print(np)
            lista_Txt[np] = "_"
            np += 1

nova_Txt = " ".join(lista_Txt)
print(nova_Txt) '''