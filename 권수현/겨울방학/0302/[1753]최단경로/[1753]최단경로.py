import sys
import heapq
input = sys.stdin.readline

v,e = map(int,input().split())
k = int(input())
graph = [[] for _ in range(v+1)]
for _ in range(e):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

distance = [float('inf')]*(v+1)
distance[k]=0
queue=[]
queue.append((0,k))
while queue:
    cost,node = heapq.heappop(queue)
    if distance[node]<cost:
        continue
    for next,dist in graph[node]:
        if distance[next]>distance[node]+dist:
            distance[next]=distance[node]+dist
            heapq.heappush(queue,(distance[next],next))

print(distance[1:])