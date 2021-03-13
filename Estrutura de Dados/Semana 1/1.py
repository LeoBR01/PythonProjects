#Exercicio 1 Estrutura de Dados , Leonardo Brasil

num = int(input("Escreva um número: "))
if num >= 1 and num <=9:
    print('Seu número está no intervalo de [1:9]')
    for i in range(1,num+1):
        for k in range(1,11):
            prod = i*k
            print(i ,'x',k,'=',prod,sep=' ')



else:
    print("Seu número vale",num,"e não está no intervalo de [1:9]")