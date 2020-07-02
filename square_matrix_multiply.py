from random import randint
import time
import timeit

tamanho_matriz = 4

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

def square_matrix_multiply_recursive(a, b):
    size = len(a)
    if size == 1:
        c = createEmptyMatrix(size)
        c[0][0] = a[0][0] * b[0][0]
        return c

    stepSize = int(size/2)

    #c11
    a11 = subMatrix(a, 0, 0, stepSize)
    a12 = subMatrix(a, 0, stepSize, stepSize)
    a21 = subMatrix(a, stepSize, 0, stepSize)
    a22 = subMatrix(a, stepSize, stepSize, stepSize)
    b11 = subMatrix(b, 0, 0, stepSize)
    b12 = subMatrix(b, 0, stepSize, stepSize)
    b21 = subMatrix(b, stepSize, 0, stepSize)
    b22 = subMatrix(b, stepSize, stepSize, stepSize)

    #c11
    c11 = matrixSum(
        square_matrix_multiply_recursive(a11, b11),
        square_matrix_multiply_recursive(a12, b21)
    )
    #c12
    c12 =  matrixSum(
        square_matrix_multiply_recursive(a11, b12),
        square_matrix_multiply_recursive(a12, b22)
    )
    #c21
    c21 = matrixSum(
        square_matrix_multiply_recursive(a21, b11),
        square_matrix_multiply_recursive(a22, b21)
    )
    #c22
    c22 = matrixSum(
        square_matrix_multiply_recursive(a21, b12),
        square_matrix_multiply_recursive(a22, b22)
    )
    return toMatrix(c11, c12, c21, c22)


def squareMatrixMultiplyDirect(a, b):
    size = len(a)
    c = createEmptyMatrix(size)
    for i in range(0, size):
        for j in range(0, size):
            res = 0
            for k in range(0, size):
                res = res + a[i][k] * b[k][j]
            c[i][j] = res
    return c

def subMatrix(m, line, col, size):
    sub = createEmptyMatrix(size)
    for i in range(0, size):
        for j in range(0, size):
            sub[i][j] = m[i + line][j + col]
    return sub

def toMatrix(c11, c12, c21, c22):
    size = len(c11)
    c = createEmptyMatrix(len(c11) * 2)
    for i in range(0, size):
        for j in range(0, size):
            c[i][j] = c11[i][j]

    for i in range(0, size):
        for j in range(0, size):
            c[i][j + size] = c12[i][j]

    for i in range(0, size):
        for j in range(0, size):
            c[i + size][j] = c21[i][j]

    for i in range(0, size):
        for j in range(0, size):
            c[i + size][j + size] = c22[i][j]
    return c


def matrixSum(c1, c2):
    size = len(c1)
    c = createEmptyMatrix(size)
    for i in range(0, size):
        for j in range(0, size):
            c[i][j] = c1[i][j] + c2[i][j]

    return c

def createEmptyMatrix(size):
    res = [None] * size
    for i in range(size):
        res[i] = [None] * size
    return res


a = gerar_matriz(tamanho_matriz)
b = gerar_matriz(tamanho_matriz)


inicio = timeit.default_timer()
c = square_matrix_multiply_recursive(a, b)
fim = timeit.default_timer()

print("Matriz A")
for x in a:
    print(x)
print("\n")
print("Matriz B")
for x in b:
    print(x)
print("\n")
print("Matriz C")
for x in c:
    print(x)
print("\n")
print ('duração da execução: %f' % (fim - inicio))