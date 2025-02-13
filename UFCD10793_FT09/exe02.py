notas = {
    "Matheus" : 20,
    "João" : 15,
    "Maria" : 18,
    "Ana" : 12,
    "José" : 10
}

notas["Leandro"] = 19
notas["Helena"] = 14

notas.pop("José")

concatenacao = " ".join(str(x) for x in notas.values())
print("Concatenação dos valores do dicionário:", concatenacao)