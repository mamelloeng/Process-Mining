idades=[25, 15, 19, 22, 37, 78, 46, 2, 67]
n = 0
for i in idades:
    if i < 18:
        n+=1
print("Existem {} pessoas menores de idade".format(n))
idades.sort(reverse=True)
print(idades)
idade = int(input("Digite uma idade: "))

# Verifica se a idade está na lista
if idade in idades:
    print("A idade está na lista")
else:
    print("Não existe ninguém com essa idade na lista")