import sys
from collections import deque
input = sys.stdin.readline

n,l,r = map(int,input().split())
a = []
for _ in range(n):
    a.append(list(map(int,input().split())))

dx = [1,-1,0,0]
dy = [0,0,1,-1]
queue = deque()

def bfs():
    sum=cnt=0
    while queue:
        y,x = queue.popleft()
        sum+=a[y][x]
        cnt+=1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n and not visited[ny][nx]:
                if  l<=abs(a[y][x]-a[ny][nx])<=r:
                    path.append((ny,nx))
                    queue.append((ny,nx))
                    visited[ny][nx]=True
    return sum//cnt

count=0
while True:
    flag=0
    visited = [[False]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                path = [(i,j)]
                queue.append((i,j))
                visited[i][j]=True
                value = bfs()

                if len(path)>1:
                    flag=1
                    for y,x in path:
                        a[y][x]=value
    if flag==0:
        break
    count+=1

print(count)