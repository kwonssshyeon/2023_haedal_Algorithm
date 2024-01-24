# 17:04 ~ (망함)
import sys
input = sys.stdin.readline

arr = []
for _ in range(19):
    arr.append(list(map(int,input().split())))

dx = [1,1,0,1]
dy = [0,1,1,-1]

for i in range(19):
    for j in range(19):

        if arr[i][j]!=0:
            color = arr[i][j]
            
            for k in range(4):
                count=1
                nx = j+dx[k]
                ny = i+dy[k]
                while 0<=nx<19 and 0<=ny<19 and arr[ny][nx]==color:
                    count+=1
                    
                    if count==5:
                        nx+=dx[k]
                        ny+=dy[k]
                        if 0<=nx<19 and 0<=ny<19 and arr[ny][nx]==color:
                            continue
                        nx = j-dx[k]
                        ny = i-dy[k]
                        if 0<=nx<19 and 0<=ny<19 and arr[ny][nx]==color:
                            continue
                        print(color)
                        print(i+1,j+1)
                        sys.exit(0)
                    nx+=dx[k]
                    ny+=dy[k]

print(0)