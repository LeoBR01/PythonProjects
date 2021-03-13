"""
Codigo main

import random

matriz1 = []
matriz2 = []
matriz3 = []

n = int(input('Digite n: '))
for i in range(n):
    linha = []
    for j in range(n):
        linha.append(random.randint(1, 20))
    matriz1.append(linha)
for i in range(n):
    linha = []
    for j in range(n):
        linha.append(random.randint(1, 20))
    matriz2.append(linha)
print('Sua matriz1 é: ', matriz1)
print('Sua matriz2 é: ', matriz2)
"""

def matriz_mult(matriz1,matriz2,n):

    for linha in range(n):
        matriz3.append([])
        for coluna in range(n):
            matriz3[linha].append(0)
            for k in range(n):
                matriz3[linha][coluna] += matriz1[linha][k] * matriz2[k][coluna]
    print(matriz3)


