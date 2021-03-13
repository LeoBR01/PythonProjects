'''
import random

matriz=[]
m = int(input('Digite m: '))
n = int(input('Digite n: '))
for i in range(m):
    linha = []
    for j in range(n):
        linha.append(random.randint(1, 50))
    matriz.append(linha)
print('sua matriz é: ', matriz)

'''

def matriz_soma(matriz,n,m):
    soma = 0
    vetor = []
    for k in range(m):
        for p in range(n):
            soma = matriz[k][p] + soma
        vetor.append(soma)
        soma = 0
    print('A soma de cada linha é: ', vetor)








