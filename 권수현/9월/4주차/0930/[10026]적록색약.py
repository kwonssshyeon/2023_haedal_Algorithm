import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
graph = []
visited=[[False]*n for _ in range(n)]
for i in range(n):
    row = list(map(str, input().strip()))
    graph.append(row)

cnt = 0
cnt_color = 0
dx = [0,0,1,-1]
dy = [1,-1,0,0]


def bfs(graph, node):
    global cnt
    queue = deque([node])
    visited[node[0]][node[1]]=True

    while queue:
        for i in range(4):
            x = queue[0][1]+dx[i]
            y = queue[0][0]+dy[i]
            if x<n and x>=0 and y<n and y>=0:
                if not visited[y][x] and graph[y][x]==graph[queue[0][0]][queue[0][1]]:
                    queue.append([y,x])
                    visited[y][x] = True

        queue.popleft()
    
    cnt+=1



def search():
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                bfs(graph,[i,j])

search()
print(cnt)

cnt=0
for i in range(n):
    for j in range(n):
        visited[i][j]=False
        if graph[i][j]=='G':
            graph[i][j]='R'

search()
print(cnt)