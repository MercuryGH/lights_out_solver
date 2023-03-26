from sage.all import *
from util import *

KERNEL_ROW_START = -2
KERNEL_ROW_END = 2
KERNEL_COL_START = -2
KERNEL_COL_END = 2
kernel = [
    [0, 0, 1, 0, 0],
    [0, 0, 2, 0, 0],
    [1, 2, 3, 2, 1],
    [0, 0, 2, 0, 0],
    [0, 0, 1, 0, 0]
]

KERNEL_ROW_START = -1
KERNEL_ROW_END = 1
KERNEL_COL_START = -1
KERNEL_COL_END = 1
kernel = [
    [0, 1, 0],
    [1, 1, 1],
    [0, 1, 0]
]

def setup_problem():
    # Problem from Hackergame 2021
    n = 12 # n_rows
    m = 12 # n_cols
    field = Zmod(256)  # GF(256)

    target = [[189, 189, 189, 189, 189, 33, 33, 33, 189, 189, 189, 189],
            [189, 189, 189, 33, 33, 33, 189, 33, 44, 189, 189, 189],
            [189, 189, 189, 189, 189, 33, 33, 33, 33, 189, 189, 189],
            [189, 189, 189, 189, 189, 33, 189, 33, 33, 189, 189, 189],
            [189, 189, 189, 33, 33, 189, 189, 33, 33, 33, 189, 189],
            [189, 134, 33, 33, 189, 189, 189, 189, 33, 33, 189, 189],
            [189, 144, 33, 33, 189, 189, 189, 189, 33, 189, 189, 189],
            [189, 142, 33, 33, 189, 189, 189, 189, 33, 33, 33, 189],
            [189, 100, 142, 33, 189, 189, 189, 189, 33, 33, 33, 189],
            [189, 142, 142, 189, 189, 189, 189, 189, 189, 33, 189, 189],
            [189, 59, 142, 33, 189, 189, 189, 189, 33, 189, 189, 189],
            [189, 189, 33, 33, 189, 189, 189, 189, 189, 189, 189, 189]]
    target_flatten = vector(field, [item for sublist in target for item in sublist])

    return n, m, field, target_flatten

def setup_problem_2():
    n = 6 # n_rows
    m = 5 # n_cols
    field = Zmod(2)  # GF(256)

    target = [[1, 1, 1, 1],
              [1, 1, 1, 1],
              [1, 1, 1, 1],
              [1, 1, 1, 1],
              [1, 1, 1, 1]]
    target_flatten = vector(field, [item for sublist in target for item in sublist])

    return n, m, field, target_flatten

def setup_problem_nm(n, m):
    field = Zmod(2)  # GF(256)

    target_flatten = vector(field, [1] * (n * m))

    return n, m, field, target_flatten

if __name__ == '__main__':
    n, m, field, target = setup_problem_nm(7, 6)

    A = Matrix(field, n * m, n * m)
    for i in range(n):
        for j in range(m):
            index = rc2id(i, j, n, m)
            for i2 in range(KERNEL_ROW_START, KERNEL_ROW_END + 1):
                for j2 in range(KERNEL_COL_START, KERNEL_COL_END + 1):
                    if rc2id(i2 + i, j2 + j, n, m) >= 0:
                        A[index, rc2id(i2 + i, j2 + j, n, m)] = kernel[i2 - KERNEL_ROW_START][j2 - KERNEL_COL_START]

    x = A.solve_left(target)
    x_mat = vec2matrix(x, n, m, field)
    
    print(x_mat)
