import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

data = []
for i in range(m):
    x,y = map(int,input().split())
    data.append([x,y])

room = [0]
for i in range(n):
    room.append(i+1)

for i in range(m):
    x = data[i][0]
    y = data[i][1]

    if x<y:
        if room[x]!=room[y]:
            point = x+1
            before = room[y]
            while point<=y:
                room[point] = room[x]
                point+=1

            j=1
            while  (y+j)<=n and room[y+j]==before:
                room[y+j]=room[y]
                j+=1


cnt=1
for i in range(1,n):
    if room[i]!=room[i+1]:
        cnt+=1
print(cnt)
    