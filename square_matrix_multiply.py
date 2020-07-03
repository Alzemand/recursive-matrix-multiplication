from random import randint
import time
import timeit

tamanho_matriz = 4

def gerar_matriz_aleatoria(tamanho):
    '''
    Função para gerar uma matriz quadrada aleatória,
    Probabilidade: 0(40%), 1(30%) ou 2(30%)
    '''
    matriz = [[] for i in range(tamanho)]
    for i in range(tamanho):
        for j in range(tamanho):
            x = randint(0, 10)
            matriz[i].append((x >= 4) + (4 <= x <= 6))
    return matriz

def square_matrix_multiply_recursive(a, b):
    size = len(a)
    if size == 1:
        return [[a[0][0] * b[0][0]]]

    step_size = int(size / 2)

    #c11
    a11 = sub_matriz(a, 0, 0, step_size)
    a12 = sub_matriz(a, 0, step_size, step_size)
    a21 = sub_matriz(a, step_size, 0, step_size)
    a22 = sub_matriz(a, step_size, step_size, step_size)
    b11 = sub_matriz(b, 0, 0, step_size)
    b12 = sub_matriz(b, 0, step_size, step_size)
    b21 = sub_matriz(b, step_size, 0, step_size)
    b22 = sub_matriz(b, step_size, step_size, step_size)

    #c11
    c11 = soma_matriz(
        square_matrix_multiply_recursive(a11, b11),
        square_matrix_multiply_recursive(a12, b21)
    )
    #c12
    c12 =  soma_matriz(
        square_matrix_multiply_recursive(a11, b12),
        square_matrix_multiply_recursive(a12, b22)
    )
    #c21
    c21 = soma_matriz(
        square_matrix_multiply_recursive(a21, b11),
        square_matrix_multiply_recursive(a22, b21)
    )
    #c22
    c22 = soma_matriz(
        square_matrix_multiply_recursive(a21, b12),
        square_matrix_multiply_recursive(a22, b22)
    )
    return criar_matriz(c11, c12, c21, c22)


def square_matrix_multiply_direct(a, b):
    size = len(a)
    c = criar_matriz_vazia(size)
    for i in range(size):
        for j in range(size):
            c[i][j] = sum(
                a[i][k] * b[k][j] for k in range(size)
            )
    return c

def sub_matriz(m, line, col, size):
    sub = criar_matriz_vazia(size)
    for i in range(size):
        for j in range(size):
            sub[i][j] = m[i + line][j + col]
    return sub

def criar_matriz(c11, c12, c21, c22):
    size = len(c11)
    c = criar_matriz_vazia(len(c11) * 2)
    for i in range(size):
        for j in range(size):
            c[i][j] = c11[i][j]

    for i in range(size):
        for j in range(size):
            c[i][j + size] = c12[i][j]

    for i in range(size):
        for j in range(size):
            c[i + size][j] = c21[i][j]

    for i in range(size):
        for j in range(size):
            c[i + size][j + size] = c22[i][j]
    return c


def soma_matriz(c1, c2):
    size = len(c1)
    return [
        [c1[i][j] + c2[i][j] for j in range(size)]
        for i in range(size)
    ]

def criar_matriz_vazia(size):
    return [[None] * size for i in range(size)]


a = gerar_matriz_aleatoria(tamanho_matriz)
b = gerar_matriz_aleatoria(tamanho_matriz)


inicio = timeit.default_timer()
c = square_matrix_multiply_recursive(a, b)
fim = timeit.default_timer()

# inicio2 = timeit.default_timer()
# c2 = square_matrix_multiply_recursive(a, b)
# fim2 = timeit.default_timer()


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
print("\n")
