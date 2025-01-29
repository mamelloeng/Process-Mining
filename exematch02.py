num1 = int(input("Digite o primeiro número\n->"))
num2 = int(input("Digite o segundo número\n->"))


operacao = input("Escolha a operação (+, -, *, /): ")


match operacao:
    case '+':
        resultado = num1 + num2
    case '-':
        resultado = num1 - num2
    case '*':
        resultado = num1 * num2
    case '/':
        if num2 == 0:
            resultado = "Divisão por zero"
        else:
            resultado = num1 / num2
    case _:
        resultado = "Operação inválida"

print('O resultado da operação é:', resultado)
