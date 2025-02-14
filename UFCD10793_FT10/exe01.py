txt = " uFcd proGRAMação eM pyTHON"

print(txt)

txt = txt.strip()
print(txt)

print(txt[:13])
print(txt[-5:])

txt = txt.upper()
print(txt)

nome = "Sandra Oliveira"
print("O {} gosta muito da {}".format(nome, txt))
print(f"O {nome} gosta muito da {txt}")