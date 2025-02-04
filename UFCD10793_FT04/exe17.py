
print("A seguir, digite 20 números reais")
s = 0
m = 0
for i in range(1, 21):
   n = int(input("Digite um número real\n->"))
   s = s + n
m = s / 20

print(f"A soma dos 20 números reais é {s}")
print(f"A média dos 20 números reais é {m}")