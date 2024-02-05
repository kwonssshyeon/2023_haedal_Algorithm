# 15:49 ~ 16:06

import sys
from collections import deque
input = sys.stdin.readline

a,b,c = map(int,input().split())
tomatoes = []
for _ in range(c):
    temp = []
    for _ in range(b):
        temp.append(list(map(int,input().split())))
    tomatoes.append(temp)
queue = deque()

dx = [0,0,1,-1,0,0]
dy = [0,0,0,0,1,-1]
dh = [1,-1,0,0,0,0]

total = a*b*c
answer=num=0

def bfs():
    global num,answer
    while queue:
        h,y,x,cnt = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nh = h + dh[i]

            if 0<=nx<a and 0<=ny<b and 0<=nh<c and tomatoes[nh][ny][nx]==0:
                tomatoes[nh][ny][nx]=1
                num+=1
                answer = cnt+1
                queue.append((nh,ny,nx,answer))
            


for i in range(c):
    for j in range(b):
        for k in range(a):
            if tomatoes[i][j][k]==1:
                queue.append((i,j,k,0))
                num+=1
            elif tomatoes[i][j][k]==-1:
                total-=1


bfs()


if num!=total:
    print(-1)
else:
    print(answer)


# msBFS ??
# 방문체크를 따로 할 필요가 업음