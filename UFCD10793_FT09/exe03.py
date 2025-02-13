import copy
Computadores_1={
 "Marca":"Asus",
 "Ecra":"14Pol",
 "RAM": [4, 8, 12]
 }

Computadores_1["Disco"] = ["128G", "256G"]

vram = int(input("Introduza a quantidade de RAM\n->"))

if vram in Computadores_1["RAM"]:
    print("RAM disponível")
else:
    print("RAM indisponível")

Computadores_1["RAM"].append(16)

Computadores_2 = copy.deepcopy(Computadores_1)

Computadores_2["Marca"] = "Lenovo"
Computadores_2["RAM"] = [4, 8]
print(Computadores_2)

Computadores_3 = copy.deepcopy(Computadores_2)
Computadores_3["Marca"] = "HP"
Computadores_3["Disco"] = ["256"]
print(Computadores_3)

Lista_Computadores = [Computadores_1, Computadores_2, Computadores_3]
print("Lista de dicionários:", Lista_Computadores)

# i. Imprimir as marcas com 128G de RAM
print("Marcas com 128G de Disco:")
for computador in Lista_Computadores:
    if "128G" in computador.get("Disco", []):
        print(computador["Marca"])

# j. Imprimir as marcas com 8 e 12 de RAM
print("Marcas com 8 e 12 de RAM:")
for computador in Lista_Computadores:
    if 8 in computador.get("RAM", []) and 12 in computador.get("RAM", []):
        print(computador["Marca"])