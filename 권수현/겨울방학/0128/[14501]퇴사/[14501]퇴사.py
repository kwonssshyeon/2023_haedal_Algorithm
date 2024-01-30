# 19:39~

import sys
input = sys.stdin.readline
n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))

dp = [0]*(n+1)

money=0
for i in range(n):
    date = i+arr[i][0]
    cost = arr[i][1]

    if date>n: continue

    for j in range(date,n+1):
        dp[j]=max(dp[i]+cost,dp[j])



print(dp[-1])



# dp
# 1+3일 이상 p를 max로 갱신
