#Implemente o algoritimo de multiplicação de matrizes recursivo.
from random import randint
import time
import timeit

tamanho_matriz = 64

#Função para gerar matriz aleatório 
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

#Função para gerar matriz nula
def gerar_matriz_nula(tamanho):
    matriz=[]
    for i in range(tamanho):
        matriz.append(i)
        matriz[i] = []
        for j in range(tamanho):
            matriz[i].append(0)
    return matriz

def mult_matriz(a, b, c, index=0):
    elemento = 0
    x = index
    for y in range(tamanho_matriz):
        for z in range(tamanho_matriz):
            elemento += a[x][z] * b[z][y]
        c[x][y] = elemento
        elemento = 0
    if (x < tamanho_matriz - 1):
        mult_matriz(a, b, c, index = index + 1)
    return c

a = gerar_matriz(tamanho_matriz)
b = gerar_matriz(tamanho_matriz)
c = gerar_matriz_nula(tamanho_matriz)

print("\n")
print("--- MATRIZ A ---")
for x in range(tamanho_matriz):
    print(a[x])

print("\n")
print("--- MATRIZ B ---")
for x in range(tamanho_matriz):
    print(b[x])

print("\n")
print("--- MATRIZ PRODUTO C ---")
inicio = timeit.default_timer()
c = mult_matriz(a, b, c)
fim = timeit.default_timer()
for x in range(tamanho_matriz):
    print(c[x])
print("\n")

print ('duração da execução: %f' % (fim - inicio))