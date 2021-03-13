#Exercicio 3 Estrutura de Dados , Leonardo Brasil


tamanho_vetor = int(input("Insira o tamanho do vetor que deseja criar: "))
vetor = []

for i in range(tamanho_vetor):
    valores_vetor = int(input("insira os valores do vetor:"))
    vetor.append(valores_vetor)

print(vetor)

max = 0
min = 0

for p in range(tamanho_vetor):
    if p == 0:
        max = min = vetor[p]
    else:
        if vetor[p] >= max:
            max = vetor[p]
        if vetor[p] <= min:
            min = vetor[p]

print('seu maximo valor é:', max)
print('seu menor valor é:', min)