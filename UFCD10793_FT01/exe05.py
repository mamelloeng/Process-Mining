a = int(input("Introduza o primeiro cateto do triângulo retângulo\n->"))
b = int(input("Introduza o segundo cateto do triângulo retângulo\n->"))
c = (a**2 + b**2)**0.5

print("O valor da hipotenusa do triângulo retângulo com catetos {} e {} é igual a: {:.2f}".format(a, b, c))