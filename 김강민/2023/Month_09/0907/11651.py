import sys
input = sys.stdin.readline

N = int(input())

position = []

for i in range(N):
    x, y = map(int, input().split())
    position.append([y, x])

sort_position = sorted(position)

for y, x in sort_position:
    print(x, y)
