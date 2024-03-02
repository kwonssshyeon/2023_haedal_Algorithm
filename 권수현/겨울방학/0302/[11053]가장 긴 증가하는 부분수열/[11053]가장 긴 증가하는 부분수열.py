import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int,input().split()))

dp = [1]*n

for i in range(n-1):
    for j in range(i+1,n):
        if nums[i]<nums[j]:
            dp[j] = max(dp[j],dp[i]+1)

print(dp)