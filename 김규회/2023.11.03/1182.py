# 1182.py
# https://www.acmicpc.net/problem/1182

from itertools import combinations
import sys
input = sys.stdin.readline

n, s = map(int, input().split())

array = list(map(int, input().split()))
ans = 0


for i in range(1, n+1):
    list = combinations(array, i)
    for j in list:
        if sum(j) == s:
            ans += 1

print(ans)