import math
import numpy as np

#Definicao: Divisão d V/B².

'''''''''
v = [250, 200, 100, 125, 150]
b = [1.31*10**(-3), 9.35*10**(-4), 1.12*10**(-3), 1.87*10**(-3), 1.50*10**(-3)]

div = [a/b**2 for a,b in zip(v,b)]

print(prod)
for i in div:
    print('{:e}'.format(i))
'''''''''

#Definicao: Calculo do erro

V = [250,200,100,125,150]
B = [1.31*pow(10,-3),9.35*pow(10,-4),1.12*pow(10,-3),1.87*pow(10,-3),1.50*pow(10,-3)]
r = [0.04,0.05,0.03,0.02,0.0275]

erro = [(2/(pow(B, 2)*pow(r, 2)))*(12.5) + (4*V/(pow(B, 3)*pow(r, 2)))*0.935*pow(10,-4) + (4*V/(pow(B, 2)*pow(r, 3)))*0.005 for V,B,r in zip(V,B,r)]
#erro_matheus = (2/(pow(B, 2)*pow(r, 2)))*(1) + (4*V/(pow(B, 3)*pow(r, 2)))*0.05*pow(10,-4) + (4*V/(pow(B, 2)*pow(r, 3)))*0.5

print(erro)
for i in erro:
    print('{:e}'.format(i))