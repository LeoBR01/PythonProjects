def bubble_sort(vetor, n):
    for i in range(n):
        bubble = i
        while bubble > 0:
            if vetor[bubble] < vetor[bubble-1]:
                aux = vetor[bubble-1]
                vetor[bubble-1] = vetor[bubble]
                vetor[bubble] = aux
                bubble = bubble-1
            else:
                bubble = 0
    return vetor


vetor = [20,13,17,-9,4,8,12]
print(bubble_sort(vetor,7))