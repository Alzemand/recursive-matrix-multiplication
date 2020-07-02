import numpy as np 
from random import randint
import time
import timeit

tamanho_matriz = 64

def gerar_matriz(tamanho):
    '''
    Função para gerar uma matriz quadrada aleatória,
    Probabilidade: 0(40%), 1(30%) ou 2(30%)
    '''
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

def dividir(matriz): 
    """ 
    Divide uma determinada matriz em quatro 
    Input: NxN  
    Output: Tupla contendo 4 n/2 x n/2 matrizes correspondendo a, b, c, d 
    """
    row, col = matriz.shape #Retorna o tamanho da matriz para o row e col
    row2, col2 = row//2, col//2
    return matriz[:row2, :col2], matriz[:row2, col2:], matriz[row2:, :col2], matriz[row2:, col2:] 
  
def matriz_mult(x, y): 
    """ 
    Multiplicação com recursividade, dividindo e conquistando 
    Input: Matriz A e Matriz B (Deve entrar com o array do numpy)
    """
    if len(x) == 1: 
        return x * y 

    # Quadrantes 
    a, b, c, d = dividir(x) 
    e, f, g, h = dividir(y) 
  
    # Produtos da multiplicação
    p1 = matriz_mult(a, f - h)   
    p2 = matriz_mult(a + b, h)         
    p3 = matriz_mult(c + d, e)         
    p4 = matriz_mult(d, g - e)         
    p5 = matriz_mult(a + d, e + h)         
    p6 = matriz_mult(b - d, g + h)   
    p7 = matriz_mult(a - c, e + f)   
    
    c11 = p5 + p4 - p2 + p6   
    c12 = p1 + p2            
    c21 = p3 + p4             
    c22 = p1 + p5 - p3 - p7   
  
    # Combinação dos 4 quadrantes da matriz horizontamente e verticalmente
    c = np.vstack((np.hstack((c11, c12)), np.hstack((c21, c22))))  
  
    return c 

a = np.array(gerar_matriz(tamanho_matriz))
b = np.array(gerar_matriz(tamanho_matriz))

inicio = timeit.default_timer()
c = matriz_mult(a, b)
fim = timeit.default_timer()

print("Matriz A")
print(a)
print("\n")
print("Matriz B")
print(b)
print("\n")
print("Matriz C")
print(c)
print("\n")
print ('duração da execução: %f' % (fim - inicio))