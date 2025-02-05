from random import random
from statistics import mean,stdev

lista = []

for num in range(101):
    lista.append(random())

print(f'Maior número: {max(lista)}')
print(f'Menor número: {min(lista)}')
print(f'Soma dos números: {sum(lista)}')
print(f'Média dos números: {mean(lista)}')
print(f'Desvio padrão dos números: {stdev(lista)}')
