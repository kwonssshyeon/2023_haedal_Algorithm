import sys
input = sys.stdin.readline

n = int(input())

# 1,2를 조합하여 n만들기 --> 조합의 개수
dp=[0]*(n+1)

if n<=2:
    print(n)
    sys.exit(0)

dp[1]=1
dp[2]=2
for i in range(3,n+1):
    dp[i] = dp[i-2]+dp[i-1]

print(dp[n]%10007)