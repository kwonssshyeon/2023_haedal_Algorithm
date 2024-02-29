import sys
from collections import deque
input = sys.stdin.readline

n,k = map(int,input().split())

visited = [False]*100001
queue = deque()
queue.append((n,0))

while queue:
    point,cnt = queue.popleft()
    
    if point==k:
        print(cnt)
        sys.exit(0)

    if 0<=point*2<100001 and not visited[point*2]:
        queue.appendleft((point*2,cnt))
        visited[point*2]=True

    if 0<=point-1<100001 and not visited[point-1]:
        queue.append((point-1,cnt+1))
        visited[point-1]=True

    if 0<=point+1<100001 and not visited[point+1]:
        queue.append((point+1,cnt+1))
        visited[point+1]=True


    
