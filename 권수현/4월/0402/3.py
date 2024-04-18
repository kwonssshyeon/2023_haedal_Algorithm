import sys
from collections import deque
input = sys.stdin.readline
n,m = map(int,input().split())
maps=[]
for _ in range(n):
    maps.append(list(map(int,input().split())))

dy = [0,0,-1,1]
dx = [1,-1,0,0]

def count_zero(y,x):
    cnt=0
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<m and 0<=ny<n:
            if maps[ny][nx]==0:
                cnt+=1

    return cnt

def bfs():
    result = []
    count = []
    while queue:
        y,x = queue.popleft()
        result.append((y,x))
        count.append(max(0,maps[y][x]-count_zero(y,x)))

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<m and 0<=ny<n and not visited[ny][nx]:
                if maps[ny][nx]>0:
                    queue.append((ny,nx))
                    visited[ny][nx]=True

    return result,count



queue = deque()
answer =0
while True:
    visited = [[False for _ in range(m)] for _ in range(n)]
    piece=0
    mountain=[]
    num = []
    flag=0
    
    for i in range(n):
        for j in range(m):
            if maps[i][j]>0 and not visited[i][j]:
                visited[i][j]=True
                queue.append((i,j))
                a,b = bfs()
                mountain+=a
                num+=b
                piece+=1
                flag=1

    for (y,x),minus in zip(mountain,num):
        maps[y][x]=minus
    
    if flag==0:
        answer=0
        break

    if piece>1:
        break
    answer+=1

print(answer)