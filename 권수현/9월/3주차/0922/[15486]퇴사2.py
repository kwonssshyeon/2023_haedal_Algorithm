import sys
input = sys.stdin.readline

n = int(input())

day = [0]
costs = [0]
for _ in range(n):
    t,p = map(int,input().split())
    day.append(t)
    costs.append(p)

dp = [0]*(n+1)

for i in range(1,n+1):
    # 현재가 큰 경우 vs 어제까지의 누적 값
    dp[i] = max(dp[i],dp[i-1])
    
    # 상담 시작일과 걸리는 날짜 수 고려
    finish = day[i]+i-1
    if finish<=n:
        # 원래 있던 값 vs 새로운 상담으로 추가된 값
        dp[finish] = max(dp[finish],dp[i-1]+costs[i])


print(max(dp))