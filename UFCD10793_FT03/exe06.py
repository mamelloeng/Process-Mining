n = float(input("Introduza um número\n->"))
n1 = float(input("Introduza outro número\n->"))
n2 = float(input("Introduza mais um número\n->"))

if n > n1 and n > n2:
    print("O primeiro número é o maior")
elif n1 > n and n1 > n2:
    print("O segundo número é o maior")
else:
    print("O terceiro número é o maior")
