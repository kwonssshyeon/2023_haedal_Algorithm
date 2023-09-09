import sys

n, e = map(int, sys.stdin.readline().split())
arr = [[sys.maxsize for r in range(n+1)] for c in range(n+1)]

for i in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    arr[a-1][b-1] = arr[b-1][a-1] = c

v1, v2 =  map(int, sys.stdin.readline().split())

def Dijkstra (s, e):
    s -= 1
    e -= 1
    included = [False for _ in range(n)]
    dists = [0 for _ in range(n)]
    for i in range(n):
        dists[i] = arr[s][i]
    
    included[s] = True
    dists[s] = 0
    while included[e] is False:
        min_dist = min(dists[i] for i in range(n) if included[i] is False)
        min_index = -1
        for i in range(n):
            if not included[i] and dists[i] == min_dist:
                min_index = i
        included[min_index] = True
        for i in range(n):
            if included[i] is False:
                dists[i] = min(dists[i], min_dist + arr[min_index][i])
    
    return dists[e]


dist1toV1 = Dijkstra(1, v1)
dist1toV2 = Dijkstra(1, v2)
distV1toV2 = Dijkstra(v1, v2)
distV1toN = Dijkstra(v1, n)
distV2toN = Dijkstra(v2, n)
if dist1toV1 == sys.maxsize or distV1toV2 == sys.maxsize or distV2toN == sys.maxsize:
    route1 = sys.maxsize
else:
    route1 = dist1toV1 + distV1toV2 + distV2toN
if dist1toV2 == sys.maxsize or distV1toV2 == sys.maxsize or distV1toN == sys.maxsize:
    route2 = sys.maxsize
else:
    route2 = dist1toV2 + distV1toV2 + distV1toN
if sys.maxsize == route1 == route2:
    print(-1)
else:
    print(min((route1, route2)))