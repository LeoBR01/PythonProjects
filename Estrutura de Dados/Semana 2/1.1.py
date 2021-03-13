def busca_menor(vetor,i,j):

    menor = i
    for k in range(i+1,j):
        if vetor[k] < vetor[menor]:
            menor = k
    return menor

#teste
#vetor = [17,-5,4,6,8,10,11,20,3,7,9,15]
#print(busca_menor(vetor,0,10))