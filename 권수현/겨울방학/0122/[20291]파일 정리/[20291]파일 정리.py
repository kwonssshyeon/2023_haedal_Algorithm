# 17:18 ~ 17:23


import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
file = defaultdict(list)

for _ in range(n):
    a,b = map(str,input().strip().split("."))
    file[b].append(a)

keys = list(file.keys())
keys.sort()

for key in keys:
    print(key, len(file[key]))

