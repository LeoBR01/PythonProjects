# Versao recursiva

def busca_binaria(vetor,menor,maior,x):
    if maior >= menor:
        meio = (maior + menor)//2
        if vetor[meio] == x:
            return meio
        elif vetor[meio] > x:
            return busca_binaria(vetor, menor, meio - 1, x)
        else:
            return busca_binaria(vetor, meio + 1, maior, x)
    else:
        return -1

#teste
#vetor = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
#print(busca_binaria(vetor,0,19,12))

