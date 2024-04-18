import sys
import heapq
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int,input().split()))
    nums.sort()

    maxi=0
    
    for i in range(1,n):
        maxi = max(maxi,nums[i]-nums[i-1])
    
    answer = maxi
    for i in range(2, n):
        answer = max(answer, abs(nums[i] - nums[i-2]))
    print(answer)