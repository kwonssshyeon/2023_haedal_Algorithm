#10819.py
# https://www.acmicpc.net/problem/10819

from itertools import permutations
import sys
input = sys.stdin.readline

n = int(input())

array = list(map(int, input().split()))
per = permutations(array)
ans = 0

# for i in per:
#     print(i)
# array.sort()

# for i in range(n):
#     print(array[i], end=' ')
    
for i in per:
    s = 0
    for j in range(len(i)-1):
        s += abs(i[j]-i[j+1])
    if s > ans:
        ans = s

print(ans)