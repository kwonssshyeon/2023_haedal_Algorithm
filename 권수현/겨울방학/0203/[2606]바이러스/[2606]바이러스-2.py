import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input())
graph={i+1:[] for i in range(n)}

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [False]*(n+1)


queue = deque()
queue.append(1)
visited[1]=True
answer=0
while queue:
    node = queue.popleft()
    for next in graph[node]:
        if not visited[next]:
            queue.append(next)
            visited[next]=True
            answer+=1

print(answer)