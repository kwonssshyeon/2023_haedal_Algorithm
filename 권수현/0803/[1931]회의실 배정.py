import sys
input = sys.stdin.readline

n = int(input())

times = []

for i in range(n):
    times.append(list(map(int, input().split())))

times.sort(key=lambda x: (x[1],x[0]))

cnt = 0
criteria = 0

for start, end  in times:
    if start >= criteria:
        cnt+=1
        criteria = end
print(cnt)