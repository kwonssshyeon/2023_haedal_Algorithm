# 14:41 ~ 15:10 (시도회수 2번/1 예외처리 안해줌)

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

arr = [[0 for _ in range(n)]for _ in range(n)]


step,num=1,1
dx = [0,1,0,-1]
dy = [-1,0,1,0]

y = x = n//2
answer = [y,x]
arr[y][x]=1
i=0
while num<n*n:
    for _ in range(step):
        num+=1
        if num> n*n:
            continue
        nx = x+dx[i]
        ny = y+dy[i]
        arr[ny][nx]=num
        if num==m:
            answer = [ny,nx]
        x,y = nx,ny 
    i+=1
    if i%2==0:
        step+=1
    if i>3:
        i-=4

for i in range(n):
    for j in range(n):
        print(arr[i][j],end=" ")
    print()

if n==1:
    for i in range(2):
        print(0,end=" ")
else:
    for i in range(2):
        print(answer[i]+1,end=" ")