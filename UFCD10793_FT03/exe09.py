nome = input("Informe o nome\n-> ")
idade = int(input("Informe a idade\n-> "))
peso = float(input("Informe o peso\n-> "))
altura = float(input("Informe a altura\n-> "))

IMC = peso/(altura**2)

if IMC < 18.5:
    print("O IMC de {} é igual a {:.2f} e está abaixo do peso".format(nome, IMC))
elif IMC < 24.9:
    print("O IMC de {} é igual a {:.2f} e está com peso normal".format(nome, IMC))
elif IMC < 29.9:
    print("O IMC de {} é igual a {:.2f} e está com excesso de peso".format(nome, IMC))
elif IMC < 34.9:
    print("O IMC de {} é igual a {:.2f} e está com obesidade grau I".format(nome, IMC))
elif IMC < 39.9:
    print("O IMC de {} é igual a {:.2f} e está com obesidade grau II".format(nome, IMC))
else:
    print("O IMC de {} é igual a {:.2f} e está com obesidade grau III".format(nome, IMC))
