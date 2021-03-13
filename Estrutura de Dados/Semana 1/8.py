#caso queira testar:
#vetor_1 = [0,1,0,0,0,0,1,0,1,1,1,1,0,1,0]
#vetor_2 = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,0,1,0,0,0,1,1,1,0,1]

c = 0
if len(vetor_1) > len(vetor_2):

    dif = len(vetor_1) - len(vetor_2)
    k = len(vetor_2)
else:
    dif = len(vetor_2) - len(vetor_1)
    k = len(vetor_1)
for i in range(1,k):
    if vetor_1[i] != vetor_2[i]:
        c += 1
c = c + dif
print('As diferenças nas posicoes sao', c)






