def squareMatrixMultiplyRecursive(a, b):
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
        squareMatrixMultiplyRecursive(a11, b11),
        squareMatrixMultiplyRecursive(a12, b21)
    )
    #c12
    c12 =  matrixSum(
        squareMatrixMultiplyRecursive(a11, b12),
        squareMatrixMultiplyRecursive(a12, b22)
    )
    #c21
    c21 = matrixSum(
        squareMatrixMultiplyRecursive(a21, b11),
        squareMatrixMultiplyRecursive(a22, b21)
    )
    #c22
    c22 = matrixSum(
        squareMatrixMultiplyRecursive(a21, b12),
        squareMatrixMultiplyRecursive(a22, b22)
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

def squareMatrixMultiplyStrassen(a, b):
    size = len(a)
    if size % 2 != 0:
        fillUpToSizePlusOne(a)
        fillUpToSizePlusOne(b)
    m = squareMatrixMultiplyStrassenRec(a, b)
    if size % 2 != 0:
        trimToSizeMinusOne(m)
    return m



def squareMatrixMultiplyStrassenRec(a, b):
    size = len(a)
    if size == 1:
        c = createEmptyMatrix(size)
        c[0][0] = a[0][0] * b[0][0]
        return c

    stepSize = int(size / 2)

    a11 = subMatrix(a, 0, 0, stepSize)
    a12 = subMatrix(a, 0, stepSize, stepSize)
    a21 = subMatrix(a, stepSize, 0, stepSize)
    a22 = subMatrix(a, stepSize, stepSize, stepSize)
    b11 = subMatrix(b, 0, 0, stepSize)
    b12 = subMatrix(b, 0, stepSize, stepSize)
    b21 = subMatrix(b, stepSize, 0, stepSize)
    b22 = subMatrix(b, stepSize, stepSize, stepSize)

    s1 = matrixSubstract(b12, b22)
    s2 = matrixSum(a11, a12)
    s3 = matrixSum(a21, a22)
    s4 = matrixSubstract(b21, b11)
    s5 = matrixSum(a11, a22)
    s6 = matrixSum(b11, b22)
    s7 = matrixSubstract(a12, a22)
    s8 = matrixSum(b21, b22)
    s9 = matrixSubstract(a11, a21)
    s10 = matrixSum(b11, b12)

    p1 = squareMatrixMultiplyStrassenRec(a11, s1)
    p2 = squareMatrixMultiplyStrassenRec(s2, b22)
    p3 = squareMatrixMultiplyStrassenRec(s3, b11)
    p4 = squareMatrixMultiplyStrassenRec(a22, s4)
    p5 = squareMatrixMultiplyStrassenRec(s5, s6)
    p6 = squareMatrixMultiplyStrassenRec(s7, s8)
    p7 = squareMatrixMultiplyStrassenRec(s9, s10)


    c11 = matrixSum(matrixSubstract(matrixSum(p5, p4), p2), p6)
    c12 = matrixSum(p1, p2)
    c21 = matrixSum(p3, p4)
    c22 = matrixSubstract(matrixSubstract(matrixSum(p5, p1), p3), p7)

    return toMatrix(c11, c12, c21, c22)



def subMatrix(m, line, col, size):
    sub = createEmptyMatrix(size)
    for i in range(0, size):
        for j in range(0, size):
            sub[i][j] = m[i + line][j + col]
    return sub

def fillUpToSizePlusOne(matrix):
    size = len(matrix)
    newSize = (size + 1)
    for i in range(0, size):
            matrix[i].append(0)
    matrix.append([0] * newSize)


def trimToSizeMinusOne(matrix):
    size = len(matrix)
    for i in range(0, size):
            del matrix[i][-1]
    del matrix[-1]


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


def matrixSum(c1, c2):
    size = len(c1)
    c = createEmptyMatrix(size)
    for i in range(0, size):
        for j in range(0, size):
            c[i][j] = c1[i][j] + c2[i][j]
    return c

def matrixSubstract(c1, c2):
    size = len(c1)
    c = createEmptyMatrix(size)
    for i in range(0, size):
        for j in range(0, size):
            c[i][j] = c1[i][j] - c2[i][j]
    return c

def createEmptyMatrix(size):
    res = [None] * size
    for i in range(size):
        res[i] = [None] * size
    return res


print(squareMatrixMultiplyDirect(
    [
        [1, 2],
        [3, 4]
    ],
    [
        [5, 6],
        [7, 8]
    ]
))

print(squareMatrixMultiplyRecursive(
    [
        [1, 2],
        [3, 4]
    ],
    [
        [5, 6],
        [7, 8]
    ]
))

print(squareMatrixMultiplyStrassen(
    [
        [1, 2],
        [3, 4]
    ],
    [
        [5, 6],
        [7, 8]
    ]
))

print(squareMatrixMultiplyDirect(
    [
        [3, 5, 9, 7],
        [2, 8, 4, 4],
        [9, 2, 8, 4],
        [3, 5, 3, 7]
    ],
    [
        [7, 1, 2, 1],
        [0, 8, 0, 1],
        [1, 5, 7, 6],
        [5, 1, 2, 0]
    ]
))

print(squareMatrixMultiplyRecursive(
    [
        [3, 5, 9, 7],
        [2, 8, 4, 4],
        [9, 2, 8, 4],
        [3, 5, 3, 7]
    ],
    [
        [7, 1, 2, 1],
        [0, 8, 0, 1],
        [1, 5, 7, 6],
        [5, 1, 2, 0]
    ]
))

print(squareMatrixMultiplyStrassen(
    [
        [3, 5, 9, 7],
        [2, 8, 4, 4],
        [9, 2, 8, 4],
        [3, 5, 3, 7]
    ],
    [
        [7, 1, 2, 1],
        [0, 8, 0, 1],
        [1, 5, 7, 6],
        [5, 1, 2, 0]
    ]
))


print(squareMatrixMultiplyDirect(
    [
        [1, 3],
        [7, 5]
    ],
    [
        [6, 8],
        [4, 2]
    ]
))

print(squareMatrixMultiplyRecursive(
    [
        [1, 3],
        [7, 5]
    ],
    [
        [6, 8],
        [4, 2]
    ]
))

print(squareMatrixMultiplyStrassen(
    [
        [1, 3],
        [7, 5]
    ],
    [
        [6, 8],
        [4, 2]
    ]
))


print(squareMatrixMultiplyDirect(
    [
        [3, 5, 9],
        [2, 8, 4],
        [9, 2, 8]
    ],
    [
        [7, 1, 2],
        [0, 8, 0],
        [1, 5, 7]
    ]
))


print(squareMatrixMultiplyStrassen(
    [
        [3, 5, 9],
        [2, 8, 4],
        [9, 2, 8]
    ],
    [
        [7, 1, 2],
        [0, 8, 0],
        [1, 5, 7]
    ]
))