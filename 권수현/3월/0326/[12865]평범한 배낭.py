import sys
input = sys.stdin.readline

n,m = map(int,input().split())

nums = [(0,0)]
for _ in range(n):
    nums.append(tuple(map(int,input().split())))

dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,m+1):
        weight,value = nums[i]
        if weight<=j:
            dp[i][j] = max(dp[i-1][j-weight]+value, dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]
print(dp[n][m])