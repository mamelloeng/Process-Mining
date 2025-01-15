a = int(input("Introduz um valor em horas\n->"))
b = int(input("Introduz um valor em minutos\n->"))
c = int(input("Introduz um valor em segundos\n->"))

d = a*3600 + b*60 + c

print("O valor total em segundos de {} horas, {} minutos e {} segundos é igual a: {}".format(a, b, c, d))