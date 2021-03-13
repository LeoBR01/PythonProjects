def soma_vetor(vetor):
    if len(vetor) == 1:
        return vetor[0]
    else:
        return vetor[0] + soma_vetor(vetor[1:])

#vetor = [1,5,8,7,9,6,3,1,5,4,0,2,3,1]
#print(soma_vetor(vetor))