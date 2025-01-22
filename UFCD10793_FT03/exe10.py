operador = input("Introduza o operador: ")
n1 = float(input("Introduza o primeiro número\n->"))
n2 = float(input("Introduza o segundo número\n->"))

if operador == "+":
    print(f"{n1} + {n2} = {n1 + n2}")
elif operador == "-":
    print(f"{n1} - {n2} = {n1 - n2}")
elif operador == "*":
    print(f"{n1} * {n2} = {n1 * n2}")
elif operador == "/":
    if n2 == 0:
        print("Não é possível dividir por zero")
    else:
        print(f"{n1} / {n2} = {n1 / n2}")
else:
    print("Operador inválido")
