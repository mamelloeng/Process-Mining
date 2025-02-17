def quadrado_p_a(l):
    area = l ** 2
    perimetro = 4 * l
    return area, perimetro

lado = int(input("Introduza o lado do quadrado\n->"))

area, perimetro = quadrado_p_a(lado)

print(f"A área do quadrado é {area} e o perímetro é {perimetro}")
