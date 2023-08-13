import sys
input = sys.stdin.readline

n = int(input())
mod = 1000000000

pre_dp=[[0]*1024 for i in range(10)]



for i in range(1,10):
    pre_dp[i][1<<i] = 1

for i in range(1,n):
    dp = [[0]*1024 for i in range(10)]
    
    for j in range(10):
        # pre_dp가 포함하는 계단 수를 모두 count하기 위함
        # 1024자리 배열을 이용하지 않고는 방법이 없을까..?
        for k in range(1024):
            if j<9:
                idx = k|(1<<(j+1))
                dp[j+1][idx] += pre_dp[j][k]
                dp[j+1][idx] %= mod
            if j>0:
                idx = k|(1<<(j-1))
                dp[j-1][idx] += pre_dp[j][k]
                dp[j-1][idx] %= mod
    pre_dp = dp


cnt=0
for i in range(10):
    cnt += pre_dp[i][1023]
    cnt %= mod

print(cnt)

