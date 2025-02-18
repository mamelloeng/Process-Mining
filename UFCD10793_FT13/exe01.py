import sys
item = 22
try:
    divisao = 1/item
    print("Valor:", item)
except (TypeError):
    print("Você deve digitar apenas números!")
    print()
except (ZeroDivisionError):
    print("Não é possível dividir por zero.")
    print()
except:
    print("Ocorreu a exceção", sys.exc_info()[0])
else:
    print("1 dividido por", item, "é", divisao)
finally:
    print("O valor fornecido foi:", item)