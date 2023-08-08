#위상정렬 연습
from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
inDegree = [0]*(n+1)
graph = [[] for i in range(n+1)]

for i in range(m):
    a,b = map(int, input().split())
    inDegree[b]+=1
    graph[a].append(b)


queue = deque()
result = []

for i in range(1, n+1):
    if inDegree[i] == 0:
        queue.append(i)


while queue:
    current = queue.popleft()
    result.append(current)
    for i in graph[current]:
        inDegree[i] -= 1
        if inDegree[i] == 0:
            queue.append(i)

print(*result, end=" ")

#어제 풀었던거랑 똑같네 ~
