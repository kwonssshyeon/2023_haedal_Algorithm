# 중복조합을 이용하지 않고 백트래킹
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
nums = list(map(int,input().split()))

nums.sort()

temp = []

def dfs(start):
    if len(temp)==m:
        print(*temp)
        return

    for i in range(start,n):
        temp.append(nums[i])
        dfs(i)
        temp.pop()

dfs(0)