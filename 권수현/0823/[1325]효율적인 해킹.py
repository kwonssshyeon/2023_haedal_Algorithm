import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())

graph=[[]for _ in range(n+1)]
for i in range(m):
    a,b = map(int,input().split())
    graph[b].append(a)




queue = deque()
maximum=0
ans = []
for i in range(1,n+1):
    visit=[0]*(n+1)

    queue.append(i)
    visit[i]=1
    cnt = 1
    while queue:
        point = queue.popleft()
        for j in graph[point]:
            if visit[j]==0:
                queue.append(j)
                visit[j]=1
                cnt+=1

    if maximum<cnt:
        maximum = cnt
        ans.clear()
        ans.append(i)
    elif maximum==cnt:
        ans.append(i)



print(*ans, end=" ")

# 왜 시간초과인지 모르겠다.. pypy로 제출하니까 맞았다고는 나옴..
