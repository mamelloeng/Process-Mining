S = 0
N = int(input("Informe a quantidade de números naturais que deseja: "))
for i in range(1, N+1):
    S = i + S
print("A soma dos {} primeiros números naturais é igual a: {}".format(N, S))