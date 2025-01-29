produto = input("produto [smartphone,tablet,laptop,outros]: \n--->")
preco = float(input("preço: \n--->"))

match produto:
    case "smartphone":
        desconto = 0.1
    case "tablet":
        desconto = 0.15
    case "laptop":
        desconto = 0.2
    case _:
        desconto = 0.0

preco_total = preco - preco * desconto

print("O preço total do produto é: {:.2f}€".format(preco_total))