import sys
input = sys.stdin.readline

num, group = map(int, input().split())
heights = list(map(int,input().split()))

difference = []
for i in range(num-1):
    difference.append(heights[i+1]-heights[i])

difference.sort()
sum = 0
for i in range(num-group):
    sum += difference[i]

print(sum)