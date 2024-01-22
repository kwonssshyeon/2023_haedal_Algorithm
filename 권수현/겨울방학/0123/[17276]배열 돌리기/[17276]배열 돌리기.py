# 1:59~2:27

import sys
input = sys.stdin.readline

# 세로선 temp로 빼두고 

T = int(input())
for _ in range(T):
    n,d = map(int,input().split())
    arr = []
    for _ in range(n):
        arr.append(list(map(int,input().split())))

    d = d%360//45
    if d<0:d+4
    
    

    for j in range(d):
        line1 = [arr[j][j] for j in range(n)]
        line2 = arr[n//2]
        line3 = [arr[n-1-j][j] for j in range(n)]
        line4 = [arr[j][n//2] for j in range(n)]

        for i in range(n):
            arr[i][i]=line2[i]
            arr[i][n-1-i]=line4[i]
            arr[i][n//2]=line1[i]
        arr[n//2]=line3
    
    for i in range(n):
        print(*arr[i])



