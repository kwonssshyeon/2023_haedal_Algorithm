# 8979.py
# https://www.acmicpc.net/problem/8979

import sys
input = sys.stdin.readline

n, k = map(int, input().split())

medal = [list(map(int, input().split())) for _ in range(n)]

medal.sort(key = lambda x : (x[1], x[2], x[3]), reverse = True)

idx = [medal[i][0] for i in range(n)].index(k)

for i in range(n):
    if medal[idx][1:] == medal[i][1:]:
        print(i+1)
        break