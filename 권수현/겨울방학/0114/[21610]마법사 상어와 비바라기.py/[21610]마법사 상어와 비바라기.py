import sys
input = sys.stdin.readline

n,m = map(int,input().split())
a = []
for _ in range(n):
    a.append(list(map(int,input().split())))
movement = []
for _ in range(m):
    movement.append(list(map(int,input().split())))

dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,-1,-1,-1,0,1,1,1]
diagonal_x = [1,1,-1,-1]
diagonal_y = [1,-1,1,-1]

visited = [[False for _ in range(n)]for _ in range(n)]

area = [[n-1,0],[n-1,1],[n-2,0],[n-2,1]]

def move(d,s):
    for i in range(len(area)):
        area[i][0]=(area[i][0]+dy[d]*s)%n
        area[i][1]=(area[i][1]+dx[d]*s)%n

        # area[i][0]+=(dy[d]*s)
        # area[i][1]+=(dx[d]*s)

        # if area[i][0]>=n:
        #     area[i][0]=area[i][0]%n
        # elif area[i][0]<0:
        #     area[i][0]=n-(abs(area[i][0])%n)
        #     area[i][0]=n-area[i][0]
        # if area[i][1]>=n:
        #     area[i][1]=area[i][1]%n
        # elif area[i][1]<0:
        #     area[i][1]=n-(abs(area[i][1])%n)
    

        a[area[i][0]][area[i][1]]+=1

def copy_water(y,x):
    count=0
    for i in range(4):
        nx = x+diagonal_x[i]
        ny = y+diagonal_y[i]
        if 0<=nx<n and 0<=ny<n and a[ny][nx]>0:
            count+=1
    
    a[y][x]+=count

def minus_water():
    global area
    temp = []
    for i in range(n):
        for j in range(n):
            if a[i][j]>=2 and not visited[i][j]:
                a[i][j]-=2
                temp.append([i,j])

    area=temp

for d,s in movement:
    move(d-1,s)
    for y,x in area:
        copy_water(y,x)
        visited[y][x]=True
    minus_water()
    visited = [[False for _ in range(n)]for _ in range(n)]


sum=0
for i in range(n):
    for j in range(n):
        sum+=a[i][j]

print(sum)