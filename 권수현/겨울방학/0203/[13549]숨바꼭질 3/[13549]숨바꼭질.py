# 20:31 ~ 21:12

import sys
from collections import deque
input = sys.stdin.readline

n,k = map(int,input().split())
visited=[-1]*(100001)

queue = deque()
queue.append(n)
visited[n]=0

while queue:
    node = queue.popleft()

    if node==k:
        print(visited[k])
        sys.exit(0)

    if 0<=node*2<100001 and visited[node*2]==-1:
        visited[node*2]=visited[node]
        queue.appendleft(node*2)

    for next in (node-1,node+1):
        if 0<=next<100001 and visited[next]==-1:
            visited[next] = visited[node]+1
            queue.append(next)
                


# 앞뒤로 움직인 횟수만 더하면 됨
# dp로 못푸는 이유??
# 그래프이론 - bfs를 이용하는 이유 : 최단경로를 계산해야해서
# 17에 먼저 도착하면 바로 멈춤
# appendleft를 해야하는 이유(2배의 경우 가중치가 0이므로 우선순위가 높음)