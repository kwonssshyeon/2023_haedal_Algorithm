import sys
input = sys.stdin.readline

n,m = map(int,input().split())
nums = sorted(list(map(int,input().split())))

temp=[]

def dfs(start):
    if len(temp)==m:
        print(*temp)
        return
    prev=0
    for i in range(start,n):
        if prev!=nums[i]:
            temp.append(nums[i])
            prev=nums[i]
            dfs(i+1)
            temp.pop()


dfs(0)

