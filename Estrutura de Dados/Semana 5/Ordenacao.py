def ordenacao(vetor, n):
    for i in range(n):
        menor = i
        for j in range(i + 1, n):
            if vetor[j] < vetor[menor]:
                menor = j
        aux = vetor[i]
        vetor[i] = vetor[menor]
        vetor[menor] = aux
    return vetor


vetor = [20,13,17,-9,4,8,2,-1,-5,0,-11,6]
vetor_ordenado = ordenacao(vetor, 12)
print(vetor_ordenado)

c = 0
for v in range(len(vetor)):
    if vetor[v] == vetor_ordenado[v]:
        c = c + 1
print('Foram feitas',c,'trocas')