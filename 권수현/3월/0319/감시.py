import sys
from copy import deepcopy
from collections import deque
input = sys.stdin.readline

n,m=map(int,input().split())
graph=[]
zero=float('inf')

for _ in range(n):
    graph.append(list(map(int,input().split())))

direct=[
    [],
    [[0],[1],[2],[3]],
    [[0,1],[2,3]],
    [[0,2],[1,2],[1,3],[0,3]],
    [[0,1,2],[0,1,3],[0,2,3],[1,2,3]],
    [[0,1,2,3]]
]

dx=[1,-1,0,0]
dy=[0,0,1,-1]

queue=deque()
def bfs(visited):
    changed=[]
    while queue:
        y,x,direct=queue.popleft()
        for i in direct:
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=ny<n and 0<=nx<m and visited[ny][nx]!=6:
                queue.append((ny,nx,[i,]))
                if visited[ny][nx]==0:
                    visited[ny][nx]='#'
                    changed.append((ny,nx))
    return visited,changed


def backtracking(depth,visited):
    global zero
    if depth==len(cctv):
        cnt = zero_count(visited)
        zero = min(zero,cnt)
        return visited

    (y,x),d = cctv[depth]

    for i in direct[d]:
        queue.append((y,x,i))
        answer,changed = bfs(visited)
        backtracking(depth+1,answer)
        for ny,nx in changed:
            visited[ny][nx]=0

        
def zero_count(visited):
    cnt=0
    for i in range(n):
        for j in range(m):
            if visited[i][j]==0:
                cnt+=1
    return cnt


cctv=[]
for i in range(n):
    for j in range(m):
        if graph[i][j]!=0 and graph[i][j]!=6:
            cctv.append(((i,j),graph[i][j]))
            
backtracking(0,deepcopy(graph))
print(zero)