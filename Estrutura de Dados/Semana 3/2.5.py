def fibonacci(n):
    if n <= 1:
        return n
    else:
        return(fibonacci(n-1) + fibonacci(n-2))
#teste
# 1,1,2,3,5,8,13,21,34,55 (valor esperado 55 -> n = 10 )
#print(fibonacci(10))
