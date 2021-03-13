#Exercicio 2 Estrutura de Dados , Leonardo Brasil


tamanho_vetor = int(input("Insira o tamanho do vetor que deseja calcular a média: "))
vetor = []
for i in range(tamanho_vetor):
    valores_vetor = int(input("insira os valores do vetor:"))
    vetor.append(valores_vetor)

k = 0
for k in vetor:
    print(k)
    k += 1

soma = 0
for p in vetor:
    soma = soma + p

print("A soma dos elementos do vetor é: ", soma)




