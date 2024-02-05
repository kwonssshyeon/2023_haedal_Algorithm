# 19:09 ~

import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
maps = [-1]*100001

queue = deque()
queue.append(n)
maps[n]=0

while queue:
    node = queue.popleft()
    if node==m:
        break

    if 0<=node*2<=100000 and maps[node*2]==-1:
        queue.appendleft(node*2)
        maps[node*2]=maps[node]

    for next in (node-1, node+1):
        if 0<=next<=100000 and maps[next]==-1:
            maps[next]=maps[node]+1
            queue.append(next)

print(maps[m])