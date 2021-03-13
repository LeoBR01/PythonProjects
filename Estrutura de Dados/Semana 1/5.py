#Exercicio 5 Estrutura de Dados , Leonardo Brasil

tamanho_vetor = int(input("Insira o tamanho do vetor que deseja criar: "))
vetor = []
for i in range(tamanho_vetor):
    valores_vetor = int(input("insira os valores do vetor:"))
    vetor.append(valores_vetor)
pares = []
impares = []

for p in vetor:
    if p % 2 == 0:
        pares.append(p)

    else:
        impares.append(p)
print("Números pares no vetor:", pares, "\nNúmeros impares no vetor:", impares)