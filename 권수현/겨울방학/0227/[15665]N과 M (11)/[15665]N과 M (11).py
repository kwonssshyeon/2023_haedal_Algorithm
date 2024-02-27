import sys
input = sys.stdin.readline

n,m = map(int,input().split())
nums = sorted(list(map(int,input().split())))

temp = []
def dfs():
    if len(temp)==m:
        print(*temp)
        return
    
    prev=0
    for i in range(n):
        if prev!=nums[i]:
            temp.append(nums[i])
            prev=nums[i]
            dfs()
            temp.pop()


dfs()