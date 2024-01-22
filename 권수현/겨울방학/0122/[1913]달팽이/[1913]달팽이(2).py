import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

arr = [[1 for _ in range(n)]for _ in range(n)]

x=y=n//2
dx=[0,1,0,-1]
dy=[-1,0,1,0]

if n==1: answer = [0,0]
else: answer = [y+1,x+1]

repeat=1
num=1
i=0
while num<=n*n:
    for _ in range(repeat):
        num+=1
        if num>n*n:break

        nx = x+dx[i]
        ny = y+dy[i]
        arr[ny][nx]=num
        if num==m:
            answer = [ny+1,nx+1]

        y,x = ny,nx
    i+=1

    if i%2==0: repeat+=1
    if i>=4: i-=4


for i in range(n):
    for j in range(n):
        print(arr[i][j],end=" ")
    print()

for i in range(2):
    print(answer[i], end=" ")