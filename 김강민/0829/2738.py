import sys
input = sys.stdin.readline

A = []
B = []

N, M = map(int, input().split())

for i in range(N):
    i = list(map(int, input().split()))
    A.append(i)

for i in range(N):
    i = list(map(int, input().split()))
    B.append(i)

for i in range(N):
    for j in range(M):
        print(A[i][j] + B[i][j], end=' ')
    print()