import sys
input = sys.stdin.readline
N = int(input())
maps=[]
for _ in range(N):
    maps.append(list(map(int,input().split())))

blue=0
white=0
def recur(y,x,n):
    global blue,white
    color = maps[y][x]
    for i in range(y,y+n):
        for j in range(x,x+n):
            if color!= maps[i][j]:
                recur(y,x,n//2)
                recur(y,x+n//2,n//2)
                recur(y+n//2,x,n//2)
                recur(y+n//2,x+n//2,n//2)
                return
    if color == 0:
        white+=1
    else:
        blue+=1


recur(0,0,N)
print(white)
print(blue)