def multiply_matrix(A, B):
    new = [[0 for _ in range(2)] for _ in range(2)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                new[i][j] += A[i][k] * B[k][j] % MOD
    return new

n = int(input())
MOD = 1000000007

matrix = [[1, 0], [0, 1]]
tmp = [[1, 1], [1, 0]]

k = 0
while 2 ** k <= n:
    if n & (1 << k):
        matrix = multiply_matrix(matrix, tmp)
    k += 1
    tmp = multiply_matrix(tmp, tmp)

print(matrix[0][1])
