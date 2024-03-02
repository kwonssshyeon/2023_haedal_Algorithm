import sys
import heapq
input = sys.stdin.readline

v,e = map(int,input().split())
k = int(input())
graph=[[]for _ in range(v+1)]
costs=[float('inf')]*(v+1)
for _ in range(e):
    u,v,w=map(int,input().split())
    graph[u].append((v,w))


queue=[]
costs[k]=0
heapq.heappush(queue,(0,k))
while queue:
    cost,node = heapq.heappop(queue)
    if costs[node]<cost:
        continue
    for next,dist in graph[node]:
        if costs[next]>dist+costs[node]:
            costs[next]=dist+costs[node]
            heapq.heappush(queue,(dist+costs[node],next))

for cost in costs[1:]:
    if cost==float('inf'):
        print('INF')
        continue
    print(cost)