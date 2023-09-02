import sys
input = sys.stdin.readline

n, total = map(int, input().split())

costs = []
for i in range(n):
    costs.append(int(input()))

costs.sort(reverse=True)

dp=[0]*(total+1)
dp[0]=1
for cost in costs:
    for i in range(cost,total+1):
        #호텔문제랑 비슷
        dp[i]+=dp[i-cost]

print(dp[total])
