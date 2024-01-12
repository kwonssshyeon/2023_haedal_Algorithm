import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
sensor = list(map(int,input().split()))

if n<=k:
    print(0)
    sys.exit()


sensor.sort()

diff = []
for i in range(1,n):
    diff.append(sensor[i]-sensor[i-1])

diff.sort()

for _ in range(k-1):
    diff.pop()

print(sum(diff))
