# 19:22 ~ 19:30

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
graph={i+1:[] for i in range(n)}

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [False]*(n+1)

answer = -1
def dfs(node):
    global answer
    visited[node]=True
    answer+=1
    for next in graph[node]:
        if not visited[next]:
            dfs(next)


dfs(1)

print(answer)