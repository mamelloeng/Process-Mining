ecivil = input("Escolha uma das inicias correspondentes ao seu estado civil:\n S\n C\n V\n4 -> ")

match ecivil:
    case 'S':
        print("Solteiro")
    case 'C':
        print("Casado")
    case 'V':
        print("Viúvo")
    case _:
        print("Estado civil inválido")

