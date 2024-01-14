import sys
from collections import deque
input = sys.stdin.readline

n,l,r = map(int,input().split())
a = []
graph = {}
for _ in range(n):
    a.append(list(map(int,input().split())))

dx = [1,-1,0,0]
dy = [0,0,1,-1]

count = 0

while True:
    flag=1
    visited = [[False for _ in range(n)]for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            graph[(i,j)]=[]
        
    # 방문여부 체크해야함
    for i in range(n):
        for j in range(n):
            if i!=n-1:
                if l<=abs(a[i][j]-a[i+1][j])<=r:
                    graph[(i,j)].append((i+1,j))
                    graph[(i+1,j)].append((i,j))
            if j!=n-1:
                if l<=abs(a[i][j]-a[i][j+1])<=r:
                    graph[(i,j)].append((i,j+1))
                    graph[(i,j+1)].append((i,j))

    queue = deque()
    sum=0
    person=0

    def bfs():
        global person
        global sum
        while queue:
            point = queue.popleft()
            x = point[1]
            y = point[0]
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                if 0<=nx<n and 0<=ny<n and visited[ny][nx]==False and (ny,nx) in graph[(y,x)]:
                    visited[ny][nx]=True
                    queue.append((ny,nx))
                    sum+=a[ny][nx]
                    person+=1
        
    for i in range(n):
        for j in range(n):
            if visited[i][j]==False:
                if len(graph[(i,j)])>0:
                    visited[i][j]=True
                    queue.append((i,j))
                    sum+=a[i][j]
                    person+=1
                    flag=0
                    bfs()
                    
                    populate = sum//person
                    for i in range(n):
                        for j in range(n):
                            if visited[i][j]:
                                a[i][j] = populate

                    sum=0
                    person=0
                    
    
    if flag==1:
        break
    count+=1

print(count)