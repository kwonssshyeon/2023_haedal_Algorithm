# 18:26 ~

import sys
input = sys.stdin.readline

n = int(input())
weights = []
for _ in range(n):
    weights.append(list(map(int,input().split())))

cost = float('inf')
temp = []
visited = [0]*n

def dfs():
    global cost
    global mini

    if len(temp)==n:
        last = weights[temp[-1]][0]
        if last>0:
            mini+=last
            cost = min(cost,mini)
            mini-=last
        return
    
    for i in range(1,n):
        if visited[i]==0:
            if weights[temp[-1]][i]==0:
                continue
            mini+=weights[temp[-1]][i]
            temp.append(i)
            visited[i] = 1
            dfs()
            visited[i] = 0
            temp.pop()
            mini-=weights[temp[-1]][i]


visited[0]=True  
temp.append(0)
mini=0
dfs()


print(cost)