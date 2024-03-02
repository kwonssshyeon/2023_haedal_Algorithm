import sys
input = sys.stdin.readline

n,m = map(int,input().split())
graph=[]
for _ in range(m):
    graph.append(tuple(map(int,input().split())))
costs=[float('inf')]*(n+1)

negative=False
costs[1]=0
for i in range(n):
    for start,end,cost in graph:
        if costs[start]!=float('inf') and costs[end]>costs[start]+cost:
            costs[end]=costs[start]+cost
            
            if i==n-1: negative=True

if negative:
    print(-1)
else:
    for c in costs[2:]:
        if c==float('inf'):
            print(-1)
        else: print(c)