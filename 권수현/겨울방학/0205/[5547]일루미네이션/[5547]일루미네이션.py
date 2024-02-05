# 19:20 ~

import sys
from collections import deque
input = sys.stdin.readline

w,h = map(int,input().split())
maps=[list(map(int,input().split()))for _ in range(h)]
visited=[[False for _ in range(w)]for _ in range(h)]

queue=deque()

def bfs():
    sum=0
    while queue:
        y,x = queue.popleft()
        if y%2==1:
            dx=[0,1,0,-1,-1,-1]
            dy=[-1,0,1,1,0,-1]
        else:
            dx=[1,1,1,0,-1,0]
            dy=[-1,0,1,1,0,-1]


        temp=6
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<w and 0<=ny<h and maps[ny][nx]:
                temp-=1
                if not visited[ny][nx]:
                    queue.append((ny,nx))
                    visited[ny][nx] = True

        sum+=temp
    return sum


def isCycle():
    sum=flag=0
    while queue:
        y,x = queue.popleft()
        if y%2==1:
            dx=[0,1,0,-1,-1,-1]
            dy=[-1,0,1,1,0,-1]
        else:
            dx=[1,1,1,0,-1,0]
            dy=[-1,0,1,1,0,-1]

        temp=6
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            if (nx<0 or nx>=w) or (ny<0 or ny>=h):
                flag=1
            
            elif maps[ny][nx]==0:
                temp-=1
                if not visited[ny][nx]:
                    queue.append((ny,nx))
                    visited[ny][nx] = True

        if flag==1: sum=0
        else: sum+=temp
    return sum

answer=0
for i in range(h):
    for j in range(w):
        if maps[i][j] and not visited[i][j]:
            queue.append((i,j))
            visited[i][j] = True
            answer+=bfs()
        elif not visited[i][j]:
            queue.append((i,j))
            visited[i][j] = True
            answer-=isCycle()


print(answer)



# y가 짝수면 dx는 -1이 3개
# 사이클 체크