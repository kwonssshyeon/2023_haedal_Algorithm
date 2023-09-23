import sys

input = sys.stdin.readline

ary = []
N = int(input())
for _ in range(N):
    E = int(input())
    if E == 0:
        ary.pop()
    else:
        ary.append(E)

print(sum(ary))
