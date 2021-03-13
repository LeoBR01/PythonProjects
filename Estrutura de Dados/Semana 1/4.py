#Exercicio 4 Estrutura de Dados , Leonardo Brasil

palavra = str(input('Escreva uma palavra: '))

a = 0
e = 0
i = 0
o = 0
u = 0

repeticao = [a,e,i,o,u]

for p in palavra:
        if p == 'a':
            a += 1
        if p == 'e':
            e += 1
        if p == 'i':
            i += 1
        if p == 'o':
            o += 1
        if p == 'u':
            u += 1


print('Quantidade de Vogais em:', palavra)
print('a:',a,
      '\ne:',e,
      '\ni:',i,
      '\no:',o,
      '\nu:',u,)






