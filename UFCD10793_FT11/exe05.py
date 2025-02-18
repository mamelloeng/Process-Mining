'''def remove_rep(lista):
    count = 0
    for i in lista:
        if i == lista[(i + 1)]:
            count += 1
    return count

lista1 = [10, "a", "a", 10, 20, 30, 40]

x = remove_rep(lista1)

print(x)'''

def remove_duplicates(lst):
    seen = set()
    unique_list = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            unique_list.append(item)
    return unique_list

# Exemplo de uso
lista = [1, 2, 2, 3, 4, 4, 5]
print(remove_duplicates(lista))  # Saída: [1, 2, 3, 4, 5]