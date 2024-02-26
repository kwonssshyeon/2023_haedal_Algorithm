import sys
from itertools import combinations_with_replacement
input = sys.stdin.readline

n,m = map(int,input().split())
nums = list(map(int,input().split()))
nums = sorted(list(set(nums)))

for i in combinations_with_replacement(nums,m):
    print(*i)