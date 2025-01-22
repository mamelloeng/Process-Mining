a = int(input("Informe um ano\n->"))

if a%4 == 0:
    if a%100 == 0:
        if a%400 == 0:
            print("O ano {} é bissexto".format(a))
        else:
            print("O ano {} não é bissexto".format(a))
    else:
        print("O ano {} é bissexto".format(a))
else:
    print("O ano {} não é bissexto".format(a))
