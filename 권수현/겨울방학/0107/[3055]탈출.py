import sys
from collections import deque
input = sys.stdin.readline

r,c = map(int,input().split())

matrix = []
queue_s = deque()
queue_w = deque()
visited_w=[[False for _ in range(c)] for _ in range(r)]
visited_s=[[False for _ in range(c)] for _ in range(r)]

for y in range(r):
    temp = list(input().strip())
    matrix.append(temp)
    for x in range(c):
        if temp[x]=='D':
            target_y = y
            target_x = x
        elif temp[x]=='S':
            queue_s.append([y,x])
            visited_s[y][x]=True
        elif temp[x]=='*':
            queue_w.append([y,x])
            visited_w[y][x]=True

dx = [1,-1,0,0]
dy = [0,0,-1,1]


count=0
find=False
while queue_s:
    count+=1


    for _ in range(len(queue_w)):
        water = queue_w.popleft()
        for i in range(4):
            ny = water[0]+dy[i]
            nx = water[1]+dx[i]
            if 0<=nx<c and 0<=ny<r and visited_w[ny][nx]!=True:
                if matrix[ny][nx]=='D' or matrix[ny][nx]=='X':
                    visited_w[ny][nx]=True
                    continue
                visited_w[ny][nx]=True
                matrix[ny][nx]='*'
                queue_w.append([ny,nx])


    for _ in range(len(queue_s)):
        start = queue_s.popleft()
        for i in range(4):
            ny = start[0]+dy[i]
            nx = start[1]+dx[i]
            if 0<=nx<c and 0<=ny<r and visited_s[ny][nx]!=True:
                if matrix[ny][nx]=='*' or matrix[ny][nx]=='X':
                    visited_s[ny][nx]=True
                    continue
                if matrix[ny][nx]=='D':
                    print(count)
                    find=True
                visited_s[ny][nx]=True
                queue_s.append([ny,nx])

    

if find==False:
    print("KAKTUS")



