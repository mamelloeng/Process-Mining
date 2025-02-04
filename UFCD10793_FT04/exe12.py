nip = int(input("Escreva um número inteiro e positivo\n->"))
fatorial = 1
for i in range(1, nip+1):
    fatorial = fatorial * i

print("O fatorial de {} é igual a: {}".format(nip, fatorial))