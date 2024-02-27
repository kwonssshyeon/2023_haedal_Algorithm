import sys
from itertools import combinations
input = sys.stdin.readline

n,m = map(int,input().split())
nums = sorted(list(map(int,input().split())))

answer = set()
for i in combinations(nums,m):
    if i not in answer:
        print(*i)
        answer.add(i)