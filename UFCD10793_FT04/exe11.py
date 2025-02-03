S = 0
P = 1
N = int(input("Informe a quantidade de números naturis\n->"))
for i in range(1, N + 1):
    S = S + i
    P = P * i
print(f"A soma dos primeiros {N} números naturais é {S}")
print(f"O produto dos primeiros {N} números naturais é {P}")