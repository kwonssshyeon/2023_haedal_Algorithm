import sys

n, m = map(int, input().split())
arr = [None] * n

for i in range(n):
    arr[i] = list(map(int, sys.stdin.readline().split()))
    for j in range(1, n):
        arr[i][j] += arr[i][j-1]

for i in range(1, n):
    for j in range(n):
        arr[i][j] += arr[i-1][j]

for i in range(m):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    x1 -= 1
    y1 -= 1
    x2 -= 1
    y2 -= 1
    sum = arr[x2][y2]
    if x1 > 0:
        sum -= arr[x1-1][y2]
    if y1 > 0:
        sum -= arr[x2][y1-1]
    if x1 > 0 and y1 > 0:
        sum += arr[x1-1][y1-1]
    print(sum)
