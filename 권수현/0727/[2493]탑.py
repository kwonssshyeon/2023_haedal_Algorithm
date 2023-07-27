import sys
input = sys.stdin.readline

n = int(input())
heights = list(map(int, input().split()))
signed = [0]*n
stack = []

for i in range(n):
    while stack:
        if stack[-1][1] > heights[i]:
            signed[i] = stack[-1][0] + 1
            break
        else:
            stack.pop()
    stack.append([i, heights[i]])

for i in range(n):
    print(signed[i], end = " ")
#print(*signed)