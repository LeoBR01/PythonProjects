def elevar(x, n):
    if n == 0:
        return 1
    else:
        return x*elevar(x, n-1)

#testar
#print(elevar(7,3))