# 17:38 ~ 17:48

import sys
import heapq
from collections import deque
input = sys.stdin.readline

n,m,start = map(int,input().split())
graph = {i+1:[] for i in range(n)}

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    # heapq.heappush(graph[a],b)
    # heapq.heappush(graph[b],a)

for key in graph.keys():
    graph[key].sort()

arr1 = []
arr2 = []

def dfs(node):
    visited[node]=True
    arr1.append(node)
    for next in graph[node]:
        if not visited[next]:
            dfs(next)



def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start]=True

    while queue:
        node = queue.popleft()
        arr2.append(node)
        for next in graph[node]:
            if not visited[next]:
                visited[next]=True
                queue.append(next)


visited=[False]*(n+1)
dfs(start)
visited=[False]*(n+1)
bfs(start)

print(*arr1)
print(*arr2)
