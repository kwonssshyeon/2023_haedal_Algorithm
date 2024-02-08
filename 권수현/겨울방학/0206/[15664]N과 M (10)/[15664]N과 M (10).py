import sys
from itertools import combinations
input = sys.stdin.readline

n,m = map(int,input().split())
nums = list(map(int,input().split()))
nums.sort()

idx = list(range(n))
result = set()
for values in combinations(idx,m):
    print(values)
    temp=[]
    for value in values:
        temp.append(nums[value])
    if tuple(temp) in result:
        continue
    result.add(tuple(temp))

for num in result:
    print(*num)

