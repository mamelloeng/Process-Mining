n1 = int(input("Escreva um número inteiro \n->"))
n2 = int(input("Escreva outro número inteiro \n->"))

if n1 > n2:
    for i in range(n2, n1+1):
        print(i)
else:
    for j in range(n1, n2+1):
        print(j)