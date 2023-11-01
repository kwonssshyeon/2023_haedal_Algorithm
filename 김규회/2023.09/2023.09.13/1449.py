# 1449번
# https://www.acmicpc.net/problem/1449

import sys
input = sys.stdin.readline

n, l = map(int, input().split())

result = 0
taped = 0

for i in sorted(list(map(int, input().split()))):
    if i > taped:
        taped = i + l - 1
        result += 1
        
print(result)