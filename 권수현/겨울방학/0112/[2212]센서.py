import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
sensor = list(map(int,input().split()))
sensor.sort()
count = n
diff = [0,]
group = [i for i in range(n)]
for i in range(1,n):
    diff.append(sensor[i]-sensor[i-1])


# 최솟값과 그것의 위치를 찾음
def find_index():
    value = float("inf")
    for i in range(1,n):
        if diff[i]<value:
            value = diff[i]
            index = i

    return value,index

def minMax(a,b):
    if a<b:
        return a,b
    else:
        return b,a

def union(p,q):
    id1,id2 = minMax(group[p],group[q])
    for idx,_ in enumerate(group):
        if group[idx]==id2:
            group[idx]=id1


while count!=k:

    min, index = find_index()
    if index<n-1:
        diff[index+1] += diff[index]
    diff[index] = float("inf")
    union(index,index-1)


    count-=1

start=0
sum=0
for i in range(1,n):
    if start!=group[i]:
        sum+=(sensor[i-1]-sensor[start])
        start=i

    elif i==n-1:
        sum+=(sensor[i]-sensor[start])

        

print(sum)