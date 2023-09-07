import sys
from collections import deque

n, target = map(int,input().split())
visited = [False]*100001
cnt = [0]*100001

queue = deque()
queue.append(n)
visited[n]=True


result = 0
while queue:
    now = queue.popleft()
    
    if now == target:
        result = cnt[target]
        break

    loc = [now-1,now+1,now*2]
    for next in loc:
        if 0<=next<100001 and visited[next]==False:
            if next == now*2:
                visited[next]=True
                cnt[next]=cnt[now]
                queue.appendleft(next)
            else:
                visited[next]=True
                cnt[next]=cnt[now]+1
                queue.append(next)

print(result)


# 너비우선탐색으로 풀었을 때 queue 에 순서대로 들어가면 안됨
# *2로 이동하는 경우 cost가 0 --> 먼저 처리
# cost가 다르면 우선순위큐로 다익스트라를 통해 구현할 수도 있다
# 일주일 안했다고 뇌가 멈췄나 ...