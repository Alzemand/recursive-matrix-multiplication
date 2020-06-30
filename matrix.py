# Multiplicação de matrizes 64x64 geradas aleatóriamente. 
# Implementação recursiva

from random import randint
from time import sleep

def gerar_matriz(tamanho):
    matriz=[]
    for i in range(tamanho):
        matriz.append(i)
        matriz[i] = []
        for j in range(tamanho):
            x = randint(0,10)
            if (x < 4):
                matriz[i].append(0)
            elif (x > 6):
                matriz[i].append(1)
            else:
                matriz[i].append(2)
    return matriz

def gerar_matriz_nula(tamanho):
    matriz=[]
    for i in range(tamanho):
        matriz.append(i)
        matriz[i] = []
        for j in range(tamanho):
            matriz[i].append(0)
    return matriz

a = [[0,2,1], [0,1,1], [1,1,0]]
b = [[0,1,0], [1,1,1], [1,1,1]]
# c = [[3,3,3], [2,2,2], [1,2,1]]
c = gerar_matriz_nula(3)

def mult_matriz(a, b, c, index=0):
    elemento = 0
    x = index
    for y in range(3):
        for z in range(3):
            elemento += a[x][z] * b[z][y]

    # if (x <= 2):
    #     mult_matriz(a, b, c, index = index + 1)
    print(elemento)

for x in range(3):
    print(a[x])

print("---")

for x in range(3):
    print(b[x])

mult_matriz(a, b, c)
