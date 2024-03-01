import sys
from collections import deque
input = sys.stdin.readline

n,m,t = map(int,input().split())

maps=[]
for _ in range(n):
    maps.append(list(map(int,input().split())))
visited = [[[False]*2 for _ in range(m)]  for _ in range(n)]
queue = deque()
dx=[1,0,-1,0]
dy=[0,1,0,-1]

mini=float('inf')



def bfs():
    global mini
    while queue:
        y,x,cnt,gram = queue.popleft()        
        if (y,x)==(n-1,m-1):
            mini = min(mini,cnt)

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<m and 0<=ny<n and not visited[ny][nx][gram]:
                if maps[ny][nx]==2:
                    gram=1
                if maps[ny][nx]==1:
                    if gram==0:
                        continue
                queue.append((ny,nx,cnt+1,gram))
                visited[ny][nx][gram]=True


queue.append((0,0,0,0))
visited[0][0][0]=True
bfs()

if mini<=t:
    print(mini)
else: print("Fail")