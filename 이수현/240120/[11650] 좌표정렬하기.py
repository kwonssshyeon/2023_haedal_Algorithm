import sys

input = sys.stdin.readline
N = int(input())
ary = []
for _ in range(N):
    ary.append(tuple(map(int, input().split())))

answer = sorted(ary, key=lambda x: (x[0], x[1]))

for i in range(N):
    print(answer[i][0], answer[i][1])
