# 10816.py
# https://www.acmicpc.net/problem/10816

import sys
input = sys.stdin.readline

n = int(input())
x = sorted(list(map(int,input().split())))
m = map(int,input().split())
y = list(map(int,input().split()))

cnt = {}

for i in x:
    if i in cnt:
        cnt[i] += 1
    else:
        cnt[i] = 1
        
for i in y:
    if i in cnt:
        print(cnt[i], end = ' ')
    else:
        print(0, end = ' ' )