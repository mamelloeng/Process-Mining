def calcular_lista(numeros):
    '''if not numeros:
        print("A lista está vazia.")
        return'''

    soma = sum(numeros)
    quantidade = len(numeros)
    media = soma / quantidade

    print(f"Soma: {soma}")
    print(f"Quantidade de elementos: {quantidade}")
    print(f"Média: {media:.2f}")


# Exemplo de uso:
numeros = [10, 20, 30, 40, 50]
calcular_lista(numeros)

