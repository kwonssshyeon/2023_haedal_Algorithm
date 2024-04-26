# 20:42 ~ 20:55
import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
maps = []
for _ in range(m):
    maps.append(tuple(map(int,input().split())))

visited = [[False for _ in range(n)]for _ in range(m)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs():
    global cnt
    while queue:
        y,x,date = queue.popleft()
        cnt+=1
        if cnt==n*m:
            return date

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m and not visited[ny][nx]:
                queue.append((ny,nx,date+1))
                visited[ny][nx]=True
        

cnt = 0
queue = deque()
for i in range(m):
    for j in range(n):
        if maps[i][j]==1:
            queue.append((i,j,0))
            visited[i][j]=True
        elif maps[i][j]==-1:
            visited[i][j]=True
            cnt+=1

answer = bfs()
print(answer if answer!=None else -1)