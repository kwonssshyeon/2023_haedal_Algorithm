import sys
input = sys.stdin.readline

n = int(input())

nums = list(map(int,input().split()))

cur_max = nums[0]
total_max = nums[0]

for i in range(1,n):
    cur_max = max(cur_max+nums[i], nums[i])
    total_max = max(cur_max,total_max)

print(total_max)
