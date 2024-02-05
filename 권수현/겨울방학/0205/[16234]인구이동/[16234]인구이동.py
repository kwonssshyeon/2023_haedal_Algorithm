# 16:35 ~ 17:24 (시간복잡도 -> 인구를 이동할 때 모든 배열을 다 탐색하지 않고 실제 이동이 필요한 부분만 저장해두고 탐색)

import sys
from collections import deque
input = sys.stdin.readline

n,l,r = map(int,input().split())
maps = []
for _ in range(n):
    maps.append(list(map(int,input().split())))
visited = [[0 for _ in range(n)]for _ in range(n)]

dx=[1,0,-1,0]
dy=[0,1,0,-1]
answer = 0
queue = deque()

def bfs():
    total=cnt=0
    while queue:
        y,x = queue.popleft()
        total+=maps[y][x]
        cnt+=1
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<n and not visited[ny][nx]:
                if l<=abs(maps[y][x]-maps[ny][nx])<=r:
                    visited[ny][nx] = visited[y][x]
                    queue.append((ny,nx))
                    
    if cnt>1:
        return total//cnt



days=0
while True:
    results = {}
    group=flag=0
    for i in range(n):
        for j in range(n):
            if visited[i][j]==0:
                group+=1
                visited[i][j]=group
                queue.append((i,j))
                
                value = bfs()
                if value:
                    results[group]=value

    if len(results)>0:
        flag=1
        for a in range(n):
            for b in range(n):
                if visited[a][b] in results:
                    maps[a][b] = results[visited[a][b]]
                visited[a][b]=0


    if flag==0:
        break
    days+=1

print(days)
