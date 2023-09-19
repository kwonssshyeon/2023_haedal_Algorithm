import sys
import math

input = sys.stdin.readline

n = int(input())

cnt=0
points=[]
for _ in range(n):
    x,y,c = list(input().split())
    
    if c=="Y":
        cnt+=1
        points.append((int(x),int(y)))


start = (1000000000,1000000000)

for point in points:
    if point[0]<start[0]:
        start = point
    elif point[0]==start[0]:
        if point[1]<start[1]:
            start = point


points.remove(start)

result = []
for point in points:
    result.append((point,math.atan2(point[1]-start[1],point[0]-start[0])))


result = sorted(result, key=lambda x:(-x[0][1],x[0][0]))
result = sorted(result, key=lambda x:x[1])

print(cnt)
print(start[0],start[1])
for i in range(cnt-1):
    print(result[i][0][0],result[i][0][1])