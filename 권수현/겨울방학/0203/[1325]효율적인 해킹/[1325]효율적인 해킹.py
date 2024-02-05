# 20:09 ~

# 시간초과를 해결하기 위한 방법??

import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
graph=[[]for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[b].append(a)

count=[0 for _ in range(n+1)]

def bfs(start):
    global answer
    queue = deque()
    queue.append(start)
    visited[start]=True
    while queue:
        node = queue.popleft()
        for next in graph[node]:
            if not visited[next]:
                queue.append(next)
                visited[next]=True
                answer+=1

result=[]
max=0
for i in range(1,n+1):
    visited=[False]*(n+1)
    answer=1
    bfs(i)
    count[i]=answer

    if max<count[i]:
        max = count[i]
        result = [i]
    elif max==count[i]:
        result.append(i)

print(*result)