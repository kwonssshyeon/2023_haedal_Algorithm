import sys

n = int(input())
m = int(input())
arr = [[sys.maxsize for col in range(n)] for row in range(n)]
for i in range(n):
    arr[i][i] = 0

# 그래프 입력
for i in range(m):
    s, e, cost = map(int, sys.stdin.readline().split())
    arr[s-1][e-1] = min(arr[s-1][e-1], cost)

# 플로이드-워셜 알고리즘
for through in range(n):
    for s in range(n):
        for e in range(n):
            arr[s][e] = min(arr[s][e], arr[s][through] + arr[through][e])

# 출력
for i in range(n):
    for j in range(n):
        if arr[i][j] == sys.maxsize:
            arr[i][j] = 0
    print(*arr[i])
