# 11053.py
# https://www.acmicpc.net/problem/11053

import sys
input = sys.stdin.readline


n = int(input())
array = list(map(int, input().split()))

# print(array[0])
dp = [1] * (n)
for i in range(1,n):
    # dp[i] = array[i-1] 
    # print(dp[i], "," ,dp[i-1])
    for j in range(i):
        if array[i] > array[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))