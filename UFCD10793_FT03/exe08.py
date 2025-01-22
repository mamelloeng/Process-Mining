a = int(input("Informe o primeiro lado do triângulo\n->"))
b = int(input("Informe o segundo lado do triângulo\n->"))
c = int(input("Informe o terceiro lado do triângulo\n->"))

if a == b and b == c:
    print("O triângulo é equilátero")
elif a == b or b == c or a == c:
    print("O triângulo é isósceles")
else:
    print("O triângulo é escaleno")
