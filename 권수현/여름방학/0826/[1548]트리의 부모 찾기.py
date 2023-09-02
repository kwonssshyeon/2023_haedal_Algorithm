import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [[] for i in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

queue = deque()
queue.append(1)

result = [0]*(n+1)

while queue:
    now = queue.popleft()
    for next in graph[now]:
        if result[next] == 0:
            result[next] = now
            queue.append(next)
    


for ans in result[2:]:
    print(ans)