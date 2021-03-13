#Versao Iterativa

def busca_binaria(vetor,menor,maior,x):

    while menor <= maior:
        meio = (maior + menor)//2
        if vetor[meio] > x:
            maior = meio - 1
        elif vetor[meio] < x:
            menor = meio + 1
        else:
            return meio
    return -1

#teste
#vetor = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
#print(busca_binaria(vetor,0,20,17))

'''

5) Como na busca binaria estamos constantemente reduzindo o tamanho do nosso vetor pela metade vamos analisar o pior caso que seria aquele a qual nosso elemento alvo está na ultima posicao do vetor ou não se encontra no mesmo.
Dessa maneira, precisariamos fazer divisoes de modo que o tamanho do nosso vetor ficaria variando da seguinte maneira : [n. n/2, n/4, n/8, ... , 1] portanto, teriamos uma quantidade de divisoes iguais a quantidade de comparacoes
que fizemos para chegar no nosso alvo. 
Vamos considerar que tenhamos feito K comparacoes, dessa maneira iremos dividir nosso vetor até seu tamanho de (n/2^k), e como vimos anteriormente essa ultima comparacao é quando realmente chegamos no nosso numero ou vimos que ele nao está contido
no vetor, logo: n/2^k = 1 -> K = log2(n)

Como começamos comparando o nosso valor alvo com o meio do vetor com tamanho total entao estamos comparando de (0 até K) portanto temos k + 1  comparacoes que em funcao de n é log2(n) +1 comparacoes! 
 
'''

'''
6) Como estamos fazendo uma busca considerando que o vetor está desordenado teriamos alguns problemas.
Na parte do codigo em que comparamos o meio do nosso vetor com o valor alvo e verificamos se é maior ou menor , estamos considerando que para facilitar a busca, todos os valores apos o meio são maiores que ele. Analogamente para
quando a situacao for de ser menor. Portanto, se o vetor está desordenado a justificativa de comparar com o meio de vetor se torna infundada, visto que, mesmo que façamos a comparacao do valor alvo com o termo medio do vetor , nao teremos 
a possibilidade de afirmar que se nosso valor alvo for maior que o meio, ele se encontrará depois do meio no vetor. O mesmo raciocionio vale para o caso do valor alvo ser menor que o valor medio. Logo, a busca binaria seria inutil nessa 
situacao de desordem do vetor.

'''