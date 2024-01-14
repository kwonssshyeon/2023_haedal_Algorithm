import sys
from collections import deque
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n,l,r = map(int,input().split())
a = []
for _ in range(n):
    a.append(list(map(int,input().split())))

dx = [1,-1,0,0]
dy = [0,0,1,-1]
path = []
visited = [[False for _ in range(n)]for _ in range(n)]

def dfs(y,x):
    global path
    visited[y][x]=True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<n and not visited[ny][nx]:
            if  l<=abs(a[y][x]-a[ny][nx])<=r:
                path.append((ny,nx))
                dfs(ny,nx)



count=0
while True:
    flag=0
    visited = [[False for _ in range(n)]for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                path = []
                path.append((i,j))
                dfs(i,j)

                if len(path)>1:
                    sum=0
                    flag=1
                    for y,x in path:
                        sum+=a[y][x]
                    population = sum//len(path)
                    for y,x in path:
                        a[y][x]=population
    if flag==0:
        break
    count+=1

print(count)