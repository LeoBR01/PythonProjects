def buscar(vetor,tamanho_vetor,numero):
    for i in range(tamanho_vetor):
        if vetor[i] == numero:
            return i
    return -1

#teste
#vetor = [1,2,3,5,9,81,10,54,74,11]
#print(buscar(vetor,9,54))

'''
2) O número máximo de comparacoes que precisamos realizar no codigo de busca é 'n'. Como o programa precisa percorrer o tamanho do vetor para que todas as possibilidade de comparacao do programa com os elementos do vetor sejam 
executadas,isso é necessario visto que, caso nao hajam todas as comparacoes entao existe a probabilidade de que o elemento que o programa nao comparou possa ser o elemento que buscamos. Dessa maneira, precisamos percorrer o tamanho 
do vetor completo para termos a certeza que nenhum elemento que sobrou era o elemento alvo da nossa busca.

'''
