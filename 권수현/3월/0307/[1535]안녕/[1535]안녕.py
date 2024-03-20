import sys
input = sys.stdin.readline

n = int(input())
L = [0]+list(map(int,input().split()))
J = [0]+list(map(int,input().split()))
dp = [[0 for _ in range(101)] for _ in range(n+1)]

for i in range(1,n+1):
    for remain in range(1,101):
        if L[i]>remain:
            dp[i][remain] = dp[i-1][remain]
        else:
            dp[i][remain] = max(dp[i-1][remain],dp[i-1][remain-L[i]]+J[i])

print(dp[n][100])

# 최대이익[i][w]
# 최대무게가 w인 가방에서 i번째 물건까지 판단했을 때의 최대 가치