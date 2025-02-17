def triangulo_analise(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return 'Não é um triângulo'
    elif a == b and b == c:
        return 'Equilátero'
    elif a == b or b == c or a == c:
        return 'Isósceles'
    else:
        return 'Escaleno'

x = int(input("Introduza o valor do primeiro lado do triângulo \n->"))
y = int(input("Introduza o valor do segundo lado do triângulo \n->"))
z = int(input("Introduza o valor do terceiro lado do triângulo \n->"))

print(triangulo_analise(x, y, z))
