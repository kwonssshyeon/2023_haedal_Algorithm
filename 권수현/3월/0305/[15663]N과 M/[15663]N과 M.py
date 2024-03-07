import sys
input = sys.stdin.readline

n,m = map(int,input().split())
nums = sorted(list(map(int,input().split())))

visited = [False]*(n+1)
temp=[]
def dfs():
    if len(temp)==m:
        print(*temp)
        return
    
    prev = 0
    for i in range(n):
        if not visited[i] and prev!=nums[i]:
            temp.append(nums[i])
            visited[i]=True
            prev = nums[i]
            dfs()
            temp.pop()
            visited[i]=False

dfs()