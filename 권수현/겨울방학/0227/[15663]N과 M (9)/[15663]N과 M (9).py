# 백트래킹(순열X)

import sys
input = sys.stdin.readline

n,m = map(int,input().split())
nums = list(map(int,input().split()))

nums.sort()

visited = [False]*n
temp = []

def dfs():
    if len(temp)==m:
        print(*temp)
        return
    
    prev = 0
    for i in range(n):
        if not visited[i] and prev!=nums[i]:
            temp.append(nums[i])
            visited[i] = True
            prev=nums[i]
            dfs()
            temp.pop()
            visited[i] = False

dfs()