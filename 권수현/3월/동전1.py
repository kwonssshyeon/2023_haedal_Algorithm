import sys
input = sys.stdin.readline

n,k = map(int,input().split())
nums=[0]
for _ in range(n):
    nums.append(int(input()))

dp = [[0 for _ in range(n+1)] for _ in range(k+1)]

for i in range(1,k+1):
    for j in range(1,n+1):
        if nums[j]<=i:
            dp[i][j] = max(dp[i-1][j],dp[i-nums[j]][j]+nums[j])
        else:
            dp[i][j] = dp[i-1][j]

for i in range(1,k+1):
    print(*dp[i])

print(dp[k][n])