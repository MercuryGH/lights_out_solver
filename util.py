from sage.all import Matrix


def id2rc(i, n, m):
    assert i >= 0
    assert i < n * m
    return (i // m, i % m)


def rc2id(r, c, n, m):
    if r < 0 or r >= n or c < 0 or c >= m:
        return -1
    return r*m + c


def vec2matrix(v, n, m, field):
    M = Matrix(field, n, m)
    for i in range(n):
        for j in range(m):
            M[i, j] = v[rc2id(i, j, n, m)]
    return M


def matrix2vec(M, n, m):
    v = []
    for i in range(n):
        for j in range(m):
            v.append(M[i, j])
    return v
