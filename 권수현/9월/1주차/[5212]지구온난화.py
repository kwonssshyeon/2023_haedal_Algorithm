import sys
import copy
input = sys.stdin.readline
n,m = map(int,input().split())

map = []
for i in range(n):
    temp = list(input().strip())
    map.append(temp)

dx = [1,-1,0,0]
dy = [0,0,-1,1]

map_cp = copy.deepcopy(map)
for y in range(n):
    for x in range(m):
        if map[y][x]=="X":
            cnt = 0
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                if 0<=nx<m and 0<=ny<n:
                    if map[ny][nx]==".":
                        cnt+=1
                else:
                     cnt+=1
            if cnt==3 or cnt==4:
                 map_cp[y][x]="."

x_start = 10
y_start = 10
x_end = 0
y_end = 0
for i in range(n):
    for j in range(m):
        if map_cp[i][j]=="X":
            x_start = min(x_start,j)
            x_end = max(x_end,j)
            y_start = min(y_start,i)
            y_end = max(y_end,i)


for i in range(y_start,y_end+1):
    for j in range(x_start,x_end+1):
        print(map_cp[i][j],end="")
    if i<y_end:
        print()