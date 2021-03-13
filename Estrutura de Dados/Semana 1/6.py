#Exercicio 6 Estrutura de Dados , Leonardo Brasil

palavra = str(input('Insira uma palavra: ')).lower()

a = 0
b = len(palavra) - 1
c = 0

for i in range(len(palavra)//2):
    if palavra[a] == palavra[b]:
        a += 1
        b -= 1
        c += 1
        if c >= (len(palavra)//2):
            print('É um palindromo')
    else:
        print('Não é um palindromo')
        break










#palindromo são palavras que podem ser lida de forma invertida que continuam gerando a mesma palavra inicial como OVO


