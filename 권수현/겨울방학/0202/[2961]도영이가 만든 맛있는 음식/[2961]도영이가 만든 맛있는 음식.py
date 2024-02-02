# 10:10~10:25

import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input())
flavors = []
for _ in range(n):
    flavors.append(tuple(map(int,input().split())))


answer = float('inf')
for i in range(1,n+1):
    for values in combinations(flavors,i):
        sour, bitter = 1,0
        for a,b in values:
            sour*=a
            bitter+=b
            temp=abs(sour-bitter)
        answer = min(temp,answer)

print(answer)