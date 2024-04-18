import sys
from collections import deque
input = sys.stdin.readline

maps=[]
for _ in range(12):
    maps.append(list(map(str,input().strip())))

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def find_four(op):
    cnt=0
    temp=[]
    while queue:
        y,x = queue.popleft()
        cnt+=1
        temp.append((y,x))
        
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<6 and 0<=ny<12 and not visited[ny][nx]:
                if maps[ny][nx]==op:
                    queue.append((ny,nx))
                    visited[ny][nx]=True
   
    if cnt>=4:
        return temp
    else: return []
        


def delete_block(deleted):
    for y,x in sorted(deleted, key=lambda x:x[0]):
        for i in range(y,0,-1):
            maps[i][x]=maps[i-1][x]
        maps[0][x]="."
        

answer=0
start=0
queue = deque()
while True:
    visited = [[False for _ in range(6)]for _ in range(12)]
    deleted = []
    flag=False
    for i in range(0,12):
        for j in range(6):
            if maps[i][j]!="." and not visited[i][j]:
                queue.append((i,j))
                visited[i][j]=True
                ans = find_four(maps[i][j])

                if len(ans)>0:
                    flag=True
                    deleted+=ans
                    prev = i


    if flag==False:
        break

    delete_block(deleted)
    answer+=1


    
print(answer)
