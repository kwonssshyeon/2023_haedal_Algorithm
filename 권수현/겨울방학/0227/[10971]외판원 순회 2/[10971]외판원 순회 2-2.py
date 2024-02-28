import sys
input = sys.stdin.readline

n = int(input())
weights = []
for _ in range(n):
    weights.append(list(map(int,input().split())))
visited = [False]*n
cnt=mini=0
cost = float('inf')

def dfs(start):
    global cnt
    global cost
    global mini
    
    if cnt==n:
        if weights[start][0]!=0:
            mini+=weights[start][0]
            cost = min(cost,mini)
            mini-=weights[start][0]
        return
    
    
    for i in range(1,n):
        if not visited[i] and weights[start][i]!=0:
            cnt+=1
            visited[i]=True
            mini+=weights[start][i]
            dfs(i)
            cnt-=1
            visited[i]=False
            mini-=weights[start][i]


visited[0]=True
cnt+=1
dfs(0)

print(cost)