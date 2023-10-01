# 1476py
# https://www.acmicpc.net/problem/1476

import sys
input = sys.stdin.readline

E,S,M, cnt = 1,1,1,1

e,s,m = map(int, input().split())

while True:
    if e == E and s == S and m == M:
        break
    
    E += 1
    S += 1
    M += 1
    cnt += 1
    if E >= 16:
        E -= 15
    if S >= 29:
        S -= 28
    if M >= 20:
        M -= 19
print(cnt)