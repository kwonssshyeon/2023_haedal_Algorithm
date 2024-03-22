import sys
input = sys.stdin.readline

n, k = map(int, input().split())

for _ in range(n):
    num = list(input().split())
    num.sort()

for i in num:
    print(i, end=' ')