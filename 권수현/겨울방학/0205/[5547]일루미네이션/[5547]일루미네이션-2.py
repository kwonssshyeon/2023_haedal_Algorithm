import sys
from collections import deque
input = sys.stdin.readline

w,h = map(int,input().split())
maps=[list(map(int,input().split()))for _ in range(h)]
visited=[[False for _ in range(w)]for _ in range(h)]


queue = deque()
def bfs():
    cnt = 0
    while queue:
        y,x = queue.popleft()
        if y%2==1 : direct = [(-1,0), (-1,-1), (0,-1), (0,1), (1,0), (1,-1)]
        else : direct = [(-1,0), (-1,1), (0,-1), (0,1), (1,0), (1,1)]
        for dy, dx in direct:
            nx = x + dx
            ny = y + dy
            if 0<=ny<h and 0<=nx<w and not visited[ny][nx]:
                if maps[ny][nx]:
                    cnt+=1
                else:
                    queue.append((ny,nx))
                    visited[ny][nx] = True
    return cnt

answer = 0
for y in (0, h-1): 
    for x in range(w):
        if maps[y][x]:
            answer += 2
            if (y==0 and x==w-1) or (y==h-1 and x==0):
                answer -= 1
        elif maps[y][x]==0 and not visited[y][x]:
            queue.append((y,x))
            visited[y][x]=True
            answer += bfs()

for y in range(h): 
    for x in (0, w-1):
        if maps[y][x]:
            if (x==0 and y%2==1) or (x==w-1 and y%2==0):
                answer +=3
            else: 
                answer +=1
        elif maps[y][x]==0 and not visited[y][x]:
            queue.append((y,x))
            visited[y][x]=True
            answer += bfs()
            
print(answer)


# maps가 0인 블럭에서 주위에 1인 블럭이 있을때마다 answer+=1
# (1일때는 visited를 true로 두지 않음)
