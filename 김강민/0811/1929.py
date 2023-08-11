import sys
input = sys.stdin.readline

M, N = map(int, input().split())

for i in range(M, N + 1):
    if i == 1:
        continue
    for x in range(x, int(i ** 0.5) + 1):
        if i % x == 0:
            break
    else:
        print(i)