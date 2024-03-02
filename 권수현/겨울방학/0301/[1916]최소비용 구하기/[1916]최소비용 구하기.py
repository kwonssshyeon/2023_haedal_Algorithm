import sys
import heapq
input = sys.stdin.readline

v = int(input())
e = int(input())
graph=[[]for _ in range(v+1)]
costs=[float('inf')]*(v+1)
for _ in range(e):
    u,v,w=map(int,input().split())
    graph[u].append((v,w))
f,t = map(int,input().split())


queue=[]
costs[f]=0
heapq.heappush(queue,(0,f))
while queue:
    cost,node = heapq.heappop(queue)
    if costs[node]<cost:
        continue
    for next,dist in graph[node]:
        if costs[next]>dist+costs[node]:
            costs[next]=dist+costs[node]
            heapq.heappush(queue,(dist+costs[node],next))


print(costs[t])