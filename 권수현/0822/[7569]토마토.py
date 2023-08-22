import sys
from collections import deque
input = sys.stdin.readline

M,N,H = map(int,input().split())

tomatoes = []
for i in range(H):
    tomato = []
    for j in range(N):
        temp = list(map(int,input().split()))
        tomato.append(temp)
    tomatoes.append(tomato)

queue = deque()
for i in range(H):
    for j in range(N):
        for k in range(M):
            if tomatoes[i][j][k]==1:
                queue.append([i,j,k])


dx = [-1,1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]


while queue:
    x,y,z = queue.popleft()

    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]
        if -1<nx<H and -1<ny<N and -1<nz<M:
            if tomatoes[nx][ny][nz]==0:
                queue.append([nx,ny,nz])
                tomatoes[nx][ny][nz] = tomatoes[x][y][z]+1
        
flag = 0
result = -1
for i in range(H):
    for j in range(N):
        for k in range(M):
            if tomatoes[i][j][k] == 0:
                flag = 1
            result = max(result,tomatoes[i][j][k])

if flag == 1:
    print(-1)
elif result == -1:
    print(0)
else:
    print(result-1)