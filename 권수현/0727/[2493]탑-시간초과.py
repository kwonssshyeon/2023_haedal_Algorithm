import sys
input = sys.stdin.readline

n = int(input())
heights = list(map(int, input().split()))
signed = [0]*n

for i in range(n-1,0,-1):
    sign = heights.pop()
    for j in range(i-1,0,-1):
        if(heights[j]>sign):
            signed[i] = j+1
            break

print(signed)