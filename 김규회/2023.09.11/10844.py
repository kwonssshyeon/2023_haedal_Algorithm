# 10844번
# https://www.acmicpc.net/problem/10844
# 2차원 배열을 생각하는 것이 중요함.
# n = 1, n = 2, n = 3 케이스를 통해서 n이 1과 2일 경우에서 활용방법을 고안하여 풀이방법을 생각해내야함.

import sys

input = sys.stdin.readline


n = int(input())

dp = [[0]*10 for _ in range(n+1)]

for i in range(1, 10):
    dp[1][i] = 1

MOD = 1000000000


for i in range(2, n+1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][1]
        elif j == 9:
            dp[i][j] = dp[i-1][8]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1] 

print(sum(dp[n]) % MOD)