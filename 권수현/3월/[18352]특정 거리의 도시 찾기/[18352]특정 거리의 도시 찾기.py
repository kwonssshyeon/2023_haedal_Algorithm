import sys
from collections import deque
input=sys.stdin.readline

n,m,k,x = map(int,input().split())
graph = [[]for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)

queue = deque()
queue.append((x,0))
visited = [-1]*(n+1)
visited[x]=0
while queue:
    node, cnt = queue.popleft()
    for next in graph[node]:
        if visited[next]==-1:
            queue.append((next,cnt+1))
            visited[next] = cnt+1


flag=0
for i,num in enumerate(visited):
    if num==k:
        print(i)
        flag=1
if flag==0:
    print(-1)