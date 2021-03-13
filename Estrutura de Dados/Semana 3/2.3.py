def busca_maior(vetor,n):
    if n == 1:
        return vetor[n]
    else:
        aux = busca_maior(vetor,n-1)
        if aux < vetor[n]:
            return vetor[n]
        else:
            return aux

#teste
#vetor = [15,5,6,3,1,54,7,89,1,100]
#print('Maior elemento é:', busca_maior(vetor,9))



