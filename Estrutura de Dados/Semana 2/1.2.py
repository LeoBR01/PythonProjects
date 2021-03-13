def busca_menor(vetor,i,j):

    menor = i
    for k in range(i+1,j):
        if vetor[k] < vetor[menor]:
            menor = k
    return menor

def ordenar(vetor,i,j):
    for k in range(i, j-1):
        menor = busca_menor(vetor,k,j)
        aux = vetor[k]
        vetor[k] = vetor[menor]
        vetor[menor] = aux
    return vetor
#teste
#vetor = [15,10,32,12,20,7,8,4,7,9,6,10,15,4,64]
#print(ordenar(vetor,0,15))
