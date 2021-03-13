def resto_divisao(x, y):
    if x < y:
        return x
    else:
        return resto_divisao(x-y, y)


#teste
#print('Resto da divisao de x/y é:', resto_divisao(10,5))
